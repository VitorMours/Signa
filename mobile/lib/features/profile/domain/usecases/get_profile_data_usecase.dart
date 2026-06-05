import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/core/entities/user_entity.dart';
import 'package:mobile/features/profile/data/repositories/profile_repository_interface_impl.dart';

class GetProfileDataUseCase {
  final ProfileRepositoryInterfaceImpl repository;

  GetProfileDataUseCase(this.repository);
  Future<UserEntity> call() async {
    try {
      UserEntity response = await repository.getUserProfileData();
      return response;
    } catch (e, stackTrace) {
      AppLogger.e("Error fetching profile data", e, stackTrace);
      rethrow;
    }
  }
}
