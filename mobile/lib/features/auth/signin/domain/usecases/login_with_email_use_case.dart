import 'package:mobile/features/auth/login/domain/entities/login_entity.dart';
import 'package:mobile/features/auth/login/domain/interfaces/login_repository_interface.dart';

class LoginWithEmailUseCase {
  final LoginRepositoryInterface _interface;
  LoginWithEmailUseCase(this._interface);

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
    return await _interface.loginWithEmail(email: email, password: password);
  }
}
