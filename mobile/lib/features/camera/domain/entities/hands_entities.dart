class HandEntity {
  final bool success;
  final List<List<Map<String, dynamic>>> hands;
  final String? gesture;

  const HandEntity({this.gesture, required this.success, required this.hands});

  List<Object?> get props => [success, gesture, hands];
}
