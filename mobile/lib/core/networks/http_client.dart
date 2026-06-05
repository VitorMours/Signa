import 'package:dio/dio.dart';
import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/core/services/auth_token_service.dart';

class HttpClient {
  final Dio dio;
  final AuthTokenService _authTokenService;

  HttpClient(this._authTokenService)
    : dio = Dio(
        BaseOptions(
          baseUrl: 'http://localhost:8000/api',
          connectTimeout: const Duration(seconds: 5),
          receiveTimeout: const Duration(seconds: 3),
        ),
      );

  // ✅ Gera o Options com o token — use só nas requisições que precisam
  Future<Options> authOptions() async {
    final token = await _authTokenService.getAccessToken();
    return Options(headers: {'Authorization': 'Bearer $token'});
  }
}
