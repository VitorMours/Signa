import 'package:mobile/core/entities/user_entity.dart';
import 'package:mobile/features/auth/login/domain/entities/login_entity.dart';

import '../interfaces/signin_repository_interface.dart';

class SigninWithEmailUseCase {
  final SigninRepositoryInterface _interface;
  SigninWithEmailUseCase(this._interface);

  Future<UserRequestEntity> call({
    required String firstName,
    required String lastName,
    required String email,
    required String password,
  }) async {
    if (email.isEmpty || password.isEmpty) {
      throw ArgumentError('Email and password are required');
    }

    if (password.length < 6) {
      throw ArgumentError("A senha precisa ser maior que 6 caracteres");
    }
     if (firstName.length < 0) {
       throw ArgumentError("Voce precisa colocar o nome do usuario");
     }

    return await _interface.signinWithEmail(firstName: firstName, lastName: lastName, email: email, password: password);
  }
}
