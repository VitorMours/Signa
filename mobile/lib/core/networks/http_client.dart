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
      ) {
    dio.interceptors.add(
      InterceptorsWrapper(
        onRequest: (options, handler) async {
          final token = await _authTokenService.getAccessToken();

          if (token != null) {
            options.headers['Authorization'] = 'Bearer $token';
            AppLogger.d("Token injetado: ${options.path}");
          }

          return handler.next(options);
        },
      ),
    );
  }
}
