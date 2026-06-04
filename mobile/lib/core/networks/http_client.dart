import 'package:dio/dio.dart';
import 'package:mobile/core/components/app_logger.dart';

class HttpClient {
  final Dio dio;

  HttpClient()
    : dio = Dio(
        BaseOptions(
          baseUrl: 'http://127.0.0.1:8000/api',
          connectTimeout: const Duration(seconds: 5),
          receiveTimeout: const Duration(seconds: 3),
        ),
      );
}
