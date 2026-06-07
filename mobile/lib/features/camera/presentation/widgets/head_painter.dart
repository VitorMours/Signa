import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:mobile/features/camera/domain/entities/head_entities.dart';

class HeadLandmarksPainter extends CustomPainter {
  final HeadEntity? headEntity;
  final bool isMirrored;

  HeadLandmarksPainter({this.headEntity, this.isMirrored = false});

  // Conexões principais do rosto (MediaPipe Face Landmarker tem 478 pontos)
  // Usando apenas o contorno principal
  static const List<List<int>> connections = [
    [10, 338],
    [338, 297],
    [297, 332],
    [332, 284],
    [284, 251],
    [251, 389],
    [389, 356],
    [356, 454],
    [454, 323],
    [323, 361],
    [361, 288],
    [288, 397],
    [397, 365],
    [365, 379],
    [379, 378],
    [378, 400],
    [400, 377],
    [377, 152],
    [152, 148],
    [148, 176],
    [176, 149],
    [149, 150],
    [150, 136],
    [136, 172],
    [172, 58],
    [58, 132],
    [132, 93],
    [93, 234],
    [234, 127],
    [127, 162],
    [162, 21],
    [21, 54],
    [54, 103],
    [103, 67],
    [67, 109],
    [109, 10],
  ];

  @override
  void paint(Canvas canvas, Size size) {
    if (headEntity == null || !headEntity!.success) return;
    if (headEntity!.faces.isEmpty) return;

    final linePaint = Paint()
      ..color = Colors.blueAccent
      ..strokeWidth = 2
      ..style = PaintingStyle.stroke;

    final pointPaint = Paint()
      ..color = Colors.lightBlueAccent
      ..style = PaintingStyle.fill;

    for (final face in headEntity!.faces) {
      final points = face.map<Offset>((landmark) {
        double dx = (landmark['x'] ?? 0.0).clamp(0.0, 1.0);
        double dy = (landmark['y'] ?? 0.0).clamp(0.0, 1.0);
        if (isMirrored) dx = 1 - dx;
        return Offset((1 - dy) * size.width, dx * size.height);
      }).toList();

      for (final connection in connections) {
        if (connection[0] < points.length && connection[1] < points.length) {
          canvas.drawLine(
            points[connection[0]],
            points[connection[1]],
            linePaint,
          );
        }
      }

      for (final point in points) {
        canvas.drawCircle(point, 2, pointPaint);
      }
    }
  }

  @override
  bool shouldRepaint(HeadLandmarksPainter oldDelegate) => true;
}
