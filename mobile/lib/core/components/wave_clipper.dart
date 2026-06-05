import 'package:flutter/material.dart';

class WaveClipper extends CustomClipper<Path> {
  @override
  Path getClip(Size size) {
    Path path = Path();

    // começa no topo esquerdo
    path.lineTo(0, 0);
    path.lineTo(size.width, 0);

    // desce até a wave
    path.lineTo(size.width, 200);

    path.quadraticBezierTo(
      size.width * 0.70,
      290,
      size.width * 0.55,
      190,
    );

    path.quadraticBezierTo(
      size.width * 0.45,
      120,
      size.width * 0.35,
      170,
    );

    path.quadraticBezierTo(
      size.width * 0.20,
      240,
      0,
      200,
    );

    path.close();

    return path;
  }

  @override
  bool shouldReclip(CustomClipper<Path> oldClipper) {
    return false;
  }
}