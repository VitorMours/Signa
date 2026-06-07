import 'package:flutter/material.dart';
import 'package:mobile/features/camera/domain/entities/pose_entities.dart';

class PoseLandmarksPainter extends CustomPainter {
  final BodyEntity? bodyEntity;
  final bool isMirrored;

  PoseLandmarksPainter({this.bodyEntity, this.isMirrored = false});

  // Conexões do MediaPipe Pose (33 landmarks)
  static const List<List<int>> connections = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 7],
    [0, 4],
    [4, 5],
    [5, 6],
    [6, 8],
    [9, 10],
    [11, 12],
    [11, 13],
    [13, 15],
    [15, 17],
    [15, 19],
    [15, 21],
    [12, 14],
    [14, 16],
    [16, 18],
    [16, 20],
    [16, 22],
    [11, 23],
    [12, 24],
    [23, 24],
    [23, 25],
    [25, 27],
    [27, 29],
    [27, 31],
    [29, 31],
    [24, 26],
    [26, 28],
    [28, 30],
    [28, 32],
    [30, 32],
  ];

  @override
  void paint(Canvas canvas, Size size) {
    print('[PosePainter] bodyEntity: $bodyEntity');

    if (bodyEntity == null || !bodyEntity!.success) return;
    final landmarks = bodyEntity!.landmarks;
    if (landmarks.isEmpty) return;

    final linePaint = Paint()
      ..color = Colors.orangeAccent
      ..strokeWidth = 3
      ..style = PaintingStyle.stroke;

    final pointPaint = Paint()
      ..color = Colors.orange
      ..style = PaintingStyle.fill;

    final circlePaint = Paint()
      ..color = Colors.orangeAccent.withOpacity(0.5)
      ..style = PaintingStyle.fill;

    final points = landmarks.map<Offset>((landmark) {
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
      canvas.drawCircle(point, 6, circlePaint);
      canvas.drawCircle(point, 3, pointPaint);
    }
  }

  @override
  bool shouldRepaint(PoseLandmarksPainter oldDelegate) => true;
}
