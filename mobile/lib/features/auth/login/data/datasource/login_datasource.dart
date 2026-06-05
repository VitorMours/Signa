import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/core/di/injection_container.dart';
import 'package:mobile/core/networks/http_client.dart';
import 'package:mobile/core/services/auth_token_service.dart';
import 'package:mobile/features/auth/login/data/models/login_model.dart';

class LoginDataSource {
  final HttpClient client;

  LoginDataSource(this.client);

  Future<LoginModel> loginWithEmail(LoginModel loginData) async {
    try {
      AppLogger.i("Trying to make login");
      final response = await client.dio.post(
        "/auth/login/",
        data: loginData.toJson(),
      );
      AppLogger.i("Login response: ${response.data}");
      await sl<AuthTokenService>().saveAccessToken(response.data["access"]);
      await sl<AuthTokenService>().saveRefreshToken(response.data["refresh"]);
      return LoginModel.fromJson(response.data);
    } catch (e, stack) {
      AppLogger.e("Login error: $e\n$stack");
      // Repropaga a exceção original para que o caller possa tratá-la
      rethrow;
    }
  }
}
