import 'package:mobile/core/entities/user_entity.dart';
import 'package:mobile/features/profile/data/datasources/profile_datasource.dart';
import 'package:mobile/features/profile/data/models/profile_model.dart';
import 'package:mobile/features/profile/domain/interfaces/profile_repository_interface.dart';

class ProfileRepositoryInterfaceImpl implements ProfileRepositoryInterface {
  final ProfileDataSource profileDataSource;
  ProfileRepositoryInterfaceImpl(this.profileDataSource);

  @override
  Future<UserEntity> getUserProfileData() async {
    final response = await profileDataSource.fetchUserProfile();
    final profileModel = ProfileModel(
      firstName: response.firstName,
      lastName: response.lastName,
      email: response.email,
      password: response.password,
    );
    return profileModel;
  }
}
