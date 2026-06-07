import 'dart:typed_data';
import 'package:camera/camera.dart';
import 'package:image/image.dart' as img;

class ImageManipulator {
  static Uint8List convertToBytes(CameraImage image) {
    if (image.format.group == ImageFormatGroup.yuv420) {
      return convertYUV420ToJpeg(image);
    }

    if (image.format.group == ImageFormatGroup.bgra8888) {
      final width = image.width;
      final height = image.height;
      final bytes = image.planes.first.bytes;
      final imgBuffer = img.Image(width: width, height: height);
      for (var y = 0; y < height; y++) {
        for (var x = 0; x < width; x++) {
          final offset = (y * width + x) * 4;
          imgBuffer.setPixelRgba(
            x,
            y,
            bytes[offset + 2],
            bytes[offset + 1],
            bytes[offset],
            bytes[offset + 3],
          );
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

  static Uint8List convertYUV420ToJpeg(CameraImage image) {
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
        final yValue = yPlane.bytes[y * yPlane.bytesPerRow + x] & 0xff;
        final uValue = uPlane.bytes[uvIndex] & 0xff;
        final vValue = vPlane.bytes[uvIndex] & 0xff;

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
}
