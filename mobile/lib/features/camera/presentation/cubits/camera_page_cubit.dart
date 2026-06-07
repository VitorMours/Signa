import 'dart:async';
import 'dart:typed_data';

import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:camera/camera.dart';
import 'package:image/image.dart' as img;
import 'package:mobile/features/camera/domain/entities/hands_entities.dart';
import 'package:mobile/features/camera/domain/entities/head_entities.dart';
import 'package:mobile/features/camera/domain/entities/pose_entities.dart';
import 'package:mobile/features/camera/domain/usecases/start_detection_usecase.dart';
import 'package:mobile/features/camera/domain/usecases/stop_detection_usecase.dart';
import 'package:mobile/utils/image_manipulator.dart';

part 'camera_page_state.dart';

class CameraPageCubit extends Cubit<CameraPageState> {
  final StartDetectionStream _startDetection;
  final StopDetectionStream _stopDetection;

  CameraController? _controller;
  StreamSubscription? _handSub;
  StreamSubscription? _bodySub;
  StreamSubscription? _headSub;

  CameraPageCubit({
    required StartDetectionStream startDetection,
    required StopDetectionStream stopDetection,
  }) : _startDetection = startDetection,
       _stopDetection = stopDetection,
       super(CameraPageInitial());

  Future<void> initCamera() async {
    emit(CameraPageLoading());
    try {
      final cameras = await availableCameras();
      final backCamera = cameras.firstWhere(
        (c) => c.lensDirection == CameraLensDirection.back,
        orElse: () => cameras.first,
      );
      _controller = CameraController(
        backCamera,
        ResolutionPreset.medium,
        enableAudio: false,
        imageFormatGroup: ImageFormatGroup.yuv420,
      );
      await _controller!.initialize();
      emit(CameraPageReady(_controller!));
    } catch (e) {
      emit(CameraPageError('Erro ao iniciar câmera: $e'));
    }
  }

  Future<void> startStreaming() async {
    if (_controller == null) return;

    try {
      await _startDetection.call();

      // ✅ Emite PRIMEIRO para garantir que o estado já é CameraPageStreaming
      emit(CameraPageStreaming(_controller!));

      // Agora registra os listeners
      _handSub = _startDetection.handStream.listen((result) {
        final current = state;
        if (current is CameraPageStreaming) {
          emit(current.copyWith(handEntity: result));
        }
      });

      _bodySub = _startDetection.bodyStream.listen((result) {
        final current = state;
        if (current is CameraPageStreaming) {
          emit(current.copyWith(bodyEntity: result));
        }
      });

      _headSub = _startDetection.headStream.listen((result) {
        final current = state;
        if (current is CameraPageStreaming) {
          emit(current.copyWith(headEntity: result));
        }
      });

      // Inicia o envio de frames
      _controller!.startImageStream((CameraImage image) {
        final bytes = ImageManipulator.convertToBytes(image);
        _startDetection.sendFrame(bytes);
      });
    } catch (e) {
      emit(CameraPageError('Erro ao iniciar streaming: $e'));
    }
  }

  Future<void> stopStreaming() async {
    await _controller?.stopImageStream();
    await _stopDetection.call();
    await _handSub?.cancel();
    await _bodySub?.cancel();
    await _headSub?.cancel();
    _handSub = null;
    _bodySub = null;
    _headSub = null;

    if (_controller != null) {
      emit(CameraPageReady(_controller!));
    }
  }

  @override
  Future<void> close() async {
    await _controller?.stopImageStream();
    await _controller?.dispose();
    await _stopDetection.call();
    await _handSub?.cancel();
    await _bodySub?.cancel();
    await _headSub?.cancel();
    super.close();
  }
}
