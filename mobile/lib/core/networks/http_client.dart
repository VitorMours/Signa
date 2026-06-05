import 'package:dio/dio.dart';
import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/core/services/auth_token_service.dart';

class HttpClient {
  final Dio dio;
  final AuthTokenService _authTokenService;

  HttpClient(this._authTokenService)
    : dio = Dio(
        BaseOptions(
          baseUrl: 'http://192.168.15.47:8000/api',
          connectTimeout: const Duration(seconds: 5),
          receiveTimeout: const Duration(seconds: 3),
        ),
      ) {
    dio.interceptors.add(
      InterceptorsWrapper(
        onError: (error, handler) async {
          // Só tenta renovar se for 401
          if (error.response?.statusCode == 401) {
            AppLogger.w("Token expirado, tentando renovar...");

            final refreshed = await _tryRefreshToken();

            if (refreshed) {
              // Repete o request original com o novo token
              final newToken = await _authTokenService.getAccessToken();
              error.requestOptions.headers['Authorization'] =
                  'Bearer $newToken';

              final response = await dio.fetch(error.requestOptions);
              return handler.resolve(
                response,
              ); // ✅ retorna o resultado do retry
            }

            // Refresh falhou — limpa os tokens
            AppLogger.e("Refresh falhou, limpando tokens...");
            await _authTokenService.saveAccessToken('');
            await _authTokenService.saveRefreshToken('');
          }

          return handler.next(error);
        },
      ),
    );
  }

  Future<Options> authOptions() async {
    final token = await _authTokenService.getAccessToken();
    return Options(headers: {'Authorization': 'Bearer $token'});
  }

  Future<bool> _tryRefreshToken() async {
    try {
      final refreshToken = await _authTokenService.getRefreshToken();
      if (refreshToken == null || refreshToken.isEmpty) return false;

      // 👇 Usa um Dio separado para evitar loop infinito
      final refreshDio = Dio(BaseOptions(baseUrl: 'http://localhost:8000/api'));

      final response = await refreshDio.post(
        '/auth/refresh/',
        data: {'refresh': refreshToken},
      );

      final newAccessToken = response.data['access'];
      await _authTokenService.saveAccessToken(newAccessToken);

      AppLogger.i("Token renovado com sucesso!");
      return true;
    } catch (e) {
      AppLogger.e("Erro ao renovar token: $e");
      return false;
    }
  }
}
