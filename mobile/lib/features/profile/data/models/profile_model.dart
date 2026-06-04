import 'package:mobile/core/entities/user_entity.dart';

class ProfileModel extends UserEntity {
  ProfileModel({
    required super.firstName,
    super.lastName,
    required super.email,
    required super.password,
  });

  factory ProfileModel.fromJson(Map<String, dynamic> json) {
    return ProfileModel(
      firstName: json['firstName'],
      lastName: json['lastName'] ?? '',
      email: json['email'],
      password: json['password'],
    );
  }

  Map<String, dynamic> toJson() => {
    "firstName": firstName,
    "lastName": lastName,
    "email": email,
    "password": password,
  };
}
