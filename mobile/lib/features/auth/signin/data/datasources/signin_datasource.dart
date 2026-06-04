import '../../../../../core/components/app_logger.dart';
import '../../../../../core/networks/http_client.dart';
import '../models/signin_model.dart';

class LoginDataSource {
  final HttpClient client;

  LoginDataSource(this.client);

  Future<SigninModel> loginWithEmail(SigninModel loginData) async {
    try {
      AppLogger.i("Trying to make login");
      final response = await client.dio.post(
        "/auth/signin/",
        data: loginData.toJson(),
      );
      AppLogger.i("Login response: ${response.data}");
      return SigninModel.fromJson(response.data);
    } catch (e, stack) {
      AppLogger.e("Login error: $e\n$stack");
      // Repropaga a exceção original para que o caller possa tratá-la
      rethrow;
    }
  }
}
