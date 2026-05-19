import 'package:mobile/features/auth/login/domain/entities/login_entity.dart';

abstract class LoginRepositoryInterface {
  Future<LoginEntity> loginWithEmail({
    required String email,
    required String password,
  });
}
