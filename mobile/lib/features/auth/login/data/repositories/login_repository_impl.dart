import 'package:mobile/features/auth/login/data/datasource/login_datasource.dart';
import 'package:mobile/features/auth/login/data/models/login_model.dart';
import 'package:mobile/features/auth/login/domain/interfaces/login_repository_interface.dart';
import 'package:mobile/features/auth/login/domain/entities/login_entity.dart';

class LoginRepositoryImpl implements LoginRepositoryInterface {

  final LoginDataSource loginDataSource;
  LoginRepositoryImpl(this.loginDataSource);


  @override
  Future<LoginEntity> loginWithEmail({required String email, required String password}) async {
    final loginModel = LoginModel(email:email, password: password);
    return await loginDataSource.loginWithEmail(loginModel);
  }
}

