import 'package:mobile/features/auth/login/domain/entities/auth_user_entity.dart';
import 'package:mobile/features/auth/login/domain/entities/login_entity.dart';
import 'package:mobile/features/auth/login/domain/interfaces/login_repository.dart';

class LoginUseCase {
  final LoginRepository repository;
  LoginUseCase(this.repository);

  Future<AuthUserEntity> call(LoginEntity loginEntity) {
    return repository.login(loginEntity.email, loginEntity.password);
  }
}
