import 'package:mobile/features/auth/login/domain/entities/auth_user_entity.dart';

abstract class LoginRepository {
  Future<AuthUserEntity> login(String email, String password);
}
