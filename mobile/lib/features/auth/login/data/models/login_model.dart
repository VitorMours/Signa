import 'package:mobile/features/auth/login/domain/entities/login_entity.dart';

class LoginModel extends LoginEntity {
  final String? accessToken;
  final String? refreshToken;

  LoginModel({
    required super.email,
    required super.password,
    this.accessToken,
    this.refreshToken,
  });

  factory LoginModel.fromJson(Map<String, dynamic> json) {
    return LoginModel(
      email: json['email'] ?? '',
      password: json['password'] ?? '',
      accessToken: json['access'],
      refreshToken: json['refresh'],
    );
  }

  Map<String, dynamic> toJson() => {"email": email, "password": password};
}
