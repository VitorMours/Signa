import 'package:mobile/core/entities/user_entity.dart';

abstract class ProfileRepositoryInterface {
  Future<UserEntity> getUserProfileData({
    required String firstName,
    String lastName,
    required String email,
    required String password,
  });
}
