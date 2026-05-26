import 'package:mobile/features/auth/login/data/repositories/login_repository_impl.dart';
import 'package:mobile/features/auth/login/domain/entities/login_entity.dart';

class LoginWithEmailUseCase {
  final LoginRepositoryImpl repository;
  LoginWithEmailUseCase(this.repository);

  Future<LoginEntity> call({
    required String email,
    required String password,
  }) async {
    if (email.isEmpty || password.isEmpty) {
      throw ArgumentError('Email and password are required');
    }

    if (password.length < 6) {
      throw ArgumentError("Password need to be bigger than 6 characters");
    }
    return await repository.loginWithEmail(email: email, password: password);
  }
}
