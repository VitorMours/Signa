import 'package:flutter/material.dart';

class WaveClipper extends CustomClipper<Path> {
  @override
  Path getClip(Size size) {
    Path path = Path();

    path.lineTo(0, 200);

    path.quadraticBezierTo(
      size.width * 0.20,
      240,
      size.width * 0.35,
      170,
    );

    path.quadraticBezierTo(
      size.width * 0.45,
      120,
      size.width * 0.55,
      190,
    );

    path.quadraticBezierTo(
      size.width * 0.70,
      290,
      size.width,
      200,
    );

    path.lineTo(size.width, size.height);

    path.lineTo(0, size.height);

    path.close();

    return path;
  }

  @override
  bool shouldReclip(CustomClipper<Path> oldClipper) {
    return false;
  }
}