import 'dart:async';
import 'dart:convert';
import 'dart:typed_data';

import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:camera/camera.dart';
import 'package:image/image.dart' as img;
import 'package:web_socket_channel/web_socket_channel.dart';
part 'camera_page_state.dart';

class CameraPageCubit extends Cubit<CameraPageState> {
  CameraController? _controller;
  WebSocketChannel? _channel;
  StreamSubscription? _webSocketSubscription;

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
      _channel = WebSocketChannel.connect(
        Uri.parse('ws://192.168.15.47:8080/v1/gesture-detection/process'),
      );

      _webSocketSubscription = _channel!.stream.listen(
        (message) {
          if (message is String) {
            try {
              final json = jsonDecode(message) as Map<String, dynamic>;
              print('[WS] keys: ${json.keys.toList()}'); // <-- add isso
              print('[WS] json completo: $json');
              emit(CameraPageStreaming(_controller!, lastResult: json));
            } catch (_) {}
          }
        },
        onError: (error) {
          emit(CameraPageError('Erro no WebSocket: $error'));
        },
        onDone: () {
          if (_controller != null) emit(CameraPageReady(_controller!));
        },
      );

      _controller!.startImageStream((CameraImage image) {
        final bytes = _convertToBytes(image);
        _channel?.sink.add(bytes);
      });

      // ✅ Emite apenas uma vez para mudar o estado de Ready → Streaming
      emit(CameraPageStreaming(_controller!));
    } catch (e) {
      emit(CameraPageError('Erro ao iniciar streaming: $e'));
    }
  }

  Future<void> stopStreaming() async {
    await _controller?.stopImageStream();
    await _webSocketSubscription?.cancel();
    _webSocketSubscription = null;
    await _channel?.sink.close();
    _channel = null;

    if (_controller != null) {
      emit(CameraPageReady(_controller!));
    }
  }

  // Converte CameraImage para bytes JPEG válidos
  Uint8List _convertToBytes(CameraImage image) {
    if (image.format.group == ImageFormatGroup.yuv420) {
      return _convertYUV420ToJpeg(image);
    }

    if (image.format.group == ImageFormatGroup.bgra8888) {
      final width = image.width;
      final height = image.height;
      final bytes = image.planes.first.bytes;
      final imgBuffer = img.Image(width: width, height: height);

      for (var y = 0; y < height; y++) {
        for (var x = 0; x < width; x++) {
          final offset = (y * width + x) * 4;
          final b = bytes[offset];
          final g = bytes[offset + 1];
          final r = bytes[offset + 2];
          final a = bytes[offset + 3];
          imgBuffer.setPixelRgba(x, y, r, g, b, a);
        }
      }
      return Uint8List.fromList(img.encodeJpg(imgBuffer, quality: 75));
    }

    final bytes = <int>[];
    for (final plane in image.planes) {
      bytes.addAll(plane.bytes);
    }
    return Uint8List.fromList(bytes);
  }

  Uint8List _convertYUV420ToJpeg(CameraImage image) {
    final yPlane = image.planes[0];
    final uPlane = image.planes[1];
    final vPlane = image.planes[2];

    final width = image.width;
    final height = image.height;
    final uvRowStride = uPlane.bytesPerRow;
    final uvPixelStride = uPlane.bytesPerPixel ?? 1;

    final imgBuffer = img.Image(width: width, height: height);

    for (var y = 0; y < height; y++) {
      for (var x = 0; x < width; x++) {
        final uvIndex = uvPixelStride * (x ~/ 2) + uvRowStride * (y ~/ 2);
        final yp = yPlane.bytes[y * yPlane.bytesPerRow + x];
        final up = uPlane.bytes[uvIndex];
        final vp = vPlane.bytes[uvIndex];

        final yValue = yp & 0xff;
        final uValue = up & 0xff;
        final vValue = vp & 0xff;

        final r = (yValue + 1.370705 * (vValue - 128)).round().clamp(0, 255);
        final g =
            (yValue - 0.337633 * (uValue - 128) - 0.698001 * (vValue - 128))
                .round()
                .clamp(0, 255);
        final b = (yValue + 1.732446 * (uValue - 128)).round().clamp(0, 255);

        imgBuffer.setPixelRgba(x, y, r, g, b, 255);
      }
    }

    return Uint8List.fromList(img.encodeJpg(imgBuffer, quality: 75));
  }

  @override
  Future<void> close() async {
    await _controller?.stopImageStream();
    await _webSocketSubscription?.cancel();
    await _controller?.dispose();
    await _channel?.sink.close();
    super.close();
  }
}
