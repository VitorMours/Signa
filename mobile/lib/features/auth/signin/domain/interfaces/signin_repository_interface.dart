import 'package:mobile/core/entities/user_entity.dart';

abstract class SigninRepositoryInterface {
  Future<UserRequestEntity> signinWithEmail({
    required String firstName,
    required String lastName,
    required String email,
    required String password,
  });
}
