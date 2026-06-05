import 'package:mobile/core/entities/user_entity.dart';

abstract class ProfileRepositoryInterface {
  Future<UserEntity> getUserProfileData();
}
