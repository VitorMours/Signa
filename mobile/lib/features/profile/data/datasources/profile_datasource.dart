import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/core/networks/http_client.dart';
import 'package:mobile/features/profile/data/models/profile_model.dart';

class ProfileDataSource {
  final HttpClient client;
  ProfileDataSource(this.client);

  Future<ProfileModel> fetchUserProfile() async {
    try {
      AppLogger.i("Fetching user profile data");
      final response = await client.dio.get('/users/');
      AppLogger.i("Profile Response: ${response.data}");
      return ProfileModel.fromJson(response.data);
    } catch (e, stack) {
      AppLogger.e("Profile error: $e\n$stack");
      rethrow;
    }
  }
}
