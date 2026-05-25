import 'package:mobile/features/auth/login/domain/entities/login_entity.dart';

class LoginModel extends LoginEntity {
  LoginModel({required super.email, required super.password});

  factory LoginModel.fromJson(Map<String, dynamic> json) {
    return LoginModel(
      email: json['email'],
      password: json['password']
    );
  }

  Map<String, dynamic> toJson() => {
    "email":email,
    "password":password,
  };
}
