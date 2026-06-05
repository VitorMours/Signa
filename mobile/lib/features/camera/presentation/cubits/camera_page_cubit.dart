import 'dart:typed_data';

import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:camera/camera.dart';
import 'package:web_socket_channel/web_socket_channel.dart';
part 'camera_page_state.dart';

class CameraPageCubit extends Cubit<CameraPageState> {
  CameraController? _controller;
  WebSocketChannel? _channel;

  CameraPageCubit() : super(CameraPageInitial());

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
        imageFormatGroup: ImageFormatGroup.jpeg,
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
      // Conecta no WebSocket
      _channel = WebSocketChannel.connect(
        Uri.parse('ws://localhost:8000/ws/stream/'),
      );

      // Inicia o stream de frames
      await _controller!.startImageStream((CameraImage image) {
        final bytes = _convertToBytes(image);
        _channel?.sink.add(bytes); // 👈 envia cada frame
      });

      emit(CameraPageStreaming(_controller!));
    } catch (e) {
      emit(CameraPageError('Erro ao iniciar streaming: $e'));
    }
  }

  Future<void> stopStreaming() async {
    await _controller?.stopImageStream();
    await _channel?.sink.close();
    _channel = null;

    if (_controller != null) {
      emit(CameraPageReady(_controller!));
    }
  }

  // Converte CameraImage para bytes
  Uint8List _convertToBytes(CameraImage image) {
    final bytes = <int>[];
    for (final plane in image.planes) {
      bytes.addAll(plane.bytes);
    }
    return Uint8List.fromList(bytes);
  }

  @override
  Future<void> close() async {
    await _controller?.stopImageStream();
    await _controller?.dispose();
    await _channel?.sink.close();
    super.close();
  }
}
