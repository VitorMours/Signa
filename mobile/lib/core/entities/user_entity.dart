
class UserRequestEntity {
  final String firstName;
  final String lastName;
  final String email ;
  final String password ;

  UserRequestEntity({
    required this.firstName,
    required this.lastName,
    required this.email,
    required this.password,
  });


  List<Object?> get props => [firstName, lastName, email, password];

}