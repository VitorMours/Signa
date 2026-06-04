import 'package:mobile/core/entities/user_entity.dart';

class SigninModel extends UserRequestEntity{
  final String? accessToken;
  final String? refreshToken;


  SigninModel({
    required this.firstName,
    required this.lastName,
    required this.email,
    required this.password,
    this.accessToken,
    this.refreshToken,
  }) : super(firstName: firstName, lastName: lastName, email: email, password: password);

  factory SigninModel.fromJson(Map<String, dynamic> json) {
    return SigninModel(
      firstName:json["first_name"] ?? '',
      lastName:json["last_name"] ?? '',
      email:json["email"] ?? '',
      password:json["password"] ?? '',
      accessToken:json["access"],
      refreshToken:json["refresh"],
    );

  }

  Map<String, dynamic> toJson() => {firstName: firstName, lastName: lastName, email: email };
}