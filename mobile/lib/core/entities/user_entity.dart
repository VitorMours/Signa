
class UserEntity {
  final String firstName;
  final String lastName;
  final String email;
  final String password;
  UserEntity({
    required this.firstName,
    this.lastName = "",
    required this.email,
    this.password = "",
  });

  List<Object?> get props => [firstName, lastName, email, password];
}

