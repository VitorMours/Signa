class BodyEntity {
  final bool success;
  final List<Map<String, double>> landmarks; // pontos do corpo
  final String? posture; // ex: "straight", "slouching"

  const BodyEntity({
    required this.success,
    required this.landmarks,
    this.posture,
  });

  List<Object?> get props => [success, posture, landmarks];
}
