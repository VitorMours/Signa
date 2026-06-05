import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/core/di/injection_container.dart';
import 'package:mobile/core/networks/http_client.dart';
import 'package:mobile/core/services/auth_token_service.dart';
import 'package:mobile/features/profile/data/models/profile_model.dart';
import 'package:jwt_decoder/jwt_decoder.dart';

class ProfileDataSource {
  final HttpClient client;
  ProfileDataSource(this.client);

  Future<ProfileModel> fetchUserProfile() async {
    AppLogger.i("Fetching user profile data");
    try {
      String? token = await sl<AuthTokenService>().getAccessToken();
      Map<String, dynamic> decodedToken = JwtDecoder.decode(token!);
      final response = await client.dio.get(
        '/users/${decodedToken['user_id']}',
        options: await client.authOptions(),
      );
      AppLogger.i("Profile Response: ${response.data}");
      return ProfileModel.fromJson(response.data);
    } catch (e, stack) {
      AppLogger.e("Profile error: $e\n$stack");
      rethrow;
    }
  }
}
