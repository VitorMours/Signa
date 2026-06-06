class Landmark {
  final double x;
  final double y;
  final double z;

  Landmark({required this.x, required this.y, required this.z});

  factory Landmark.fromJson(Map<String, dynamic> json) {
    return Landmark(
      x: json['x'].toDouble(),
      y: json['y'].toDouble(),
      z: json['z'].toDouble(),
    );
  }
}
