import 'package:mobile/core/entities/user_entity.dart';

class ProfileModel extends UserEntity {
  ProfileModel({
    required super.firstName,
    super.lastName,
    required super.email,
    super.password,
  });

  factory ProfileModel.fromJson(Map<String, dynamic> json) {
    return ProfileModel(
      firstName: json['first_name'] ?? json['firstName'] ?? '',
      lastName: json['last_name'] ?? json['lastName'] ?? '',
      email: json['email'] ?? '',
      password: json['password'] ?? '',
    );
  }

  Map<String, dynamic> toJson() => {
    "first_name": firstName,
    "last_name": lastName,
    "email": email,
    "password": password,
  };
}
