import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:mobile/features/camera/data/models/landmark_model.dart';

class HandLandmarksPainter extends CustomPainter {
  final List<List<Map<String, dynamic>>> hands;
  final Size? previewSize;
  final bool isMirrored;

  HandLandmarksPainter(this.hands, {this.previewSize, this.isMirrored = false});

  static const List<List<int>> connections = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [0, 5],
    [5, 6],
    [6, 7],
    [7, 8],
    [5, 9],
    [9, 10],
    [10, 11],
    [11, 12],
    [9, 13],
    [13, 14],
    [14, 15],
    [15, 16],
    [13, 17],
    [17, 18],
    [18, 19],
    [19, 20],
    [0, 17],
  ];

  @override
  void paint(Canvas canvas, Size size) {
    print('[PosePainter] bodyEntity: $hands');

    if (hands.isEmpty) return;

    final linePaint = Paint()
      ..color = Colors.lightGreenAccent
      ..strokeWidth = 4
      ..style = PaintingStyle.stroke;

    final pointPaint = Paint()
      ..color = Colors.yellow
      ..style = PaintingStyle.fill;

    final circlePaint = Paint()
      ..color = Colors.greenAccent.withOpacity(0.6)
      ..style = PaintingStyle.fill;

    for (final hand in hands) {
      final points = hand.map<Offset>((landmark) {
        double dx = _toDouble(landmark['x']).clamp(0.0, 1.0);
        double dy = _toDouble(landmark['y']).clamp(0.0, 1.0);
        if (isMirrored) dx = 1 - dx;

        // rotaciona 90° no sentido horário
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
        canvas.drawCircle(point, 8, circlePaint);
        canvas.drawCircle(point, 4, pointPaint);
      }
    }
  }

  double _toDouble(dynamic value) {
    if (value is double) return value;
    if (value is int) return value.toDouble();
    if (value is String) return double.tryParse(value) ?? 0.0;
    return 0.0;
  }

  @override
  bool shouldRepaint(HandLandmarksPainter oldDelegate) => true;
}
