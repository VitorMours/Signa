class HeadEntity {
  final bool success;
  final List<List<Map<String, double>>>
  faces; // lista de faces, cada face tem landmarks
  final String? orientation;

  const HeadEntity({
    required this.success,
    required this.faces, // lista de faces, cada face tem landmarks
    this.orientation,
  });

  List<Object?> get props => [success, orientation, faces];
}
