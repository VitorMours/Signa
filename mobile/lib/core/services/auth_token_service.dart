import 'package:hive/hive.dart';
import 'package:mobile/core/components/app_logger.dart';
import 'package:shared_preferences/shared_preferences.dart';

class AuthTokenService {
  static late Box<String> authBox;

  Future<void> initDependencies() async {
    authBox = await Hive.openBox<String>("auth_token");
  }

  Future<void> saveAccessToken(String token) async {
    await authBox.put("access_token", token);
    AppLogger.d("Dados foram inseridos dentro do access_token");
  }

  Future<void> saveRefreshToken(String token) async {
    await authBox.put("refresh_token", token);
    AppLogger.d("Dados foram inseridos dentro do refresh_token");
  }

  Future<String?> getAccessToken() async {
    AppLogger.d("Dados lidos diretamente do access_token");
    return authBox.get("access_token");
  }

  Future<String?> getRefreshToken() async {
    AppLogger.d("Dados lidos diretamente do refresh_token");
    return authBox.get("refresh_token");
  }
}
