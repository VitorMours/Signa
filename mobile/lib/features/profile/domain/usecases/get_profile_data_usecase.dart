import 'package:mobile/core/entities/user_entity.dart';
import 'package:mobile/features/profile/data/repositories/profile_repository_interface_impl.dart';

class GetProfileDataUseCase {
  final ProfileRepositoryInterfaceImpl repository;

  GetProfileDataUseCase(this.repository);

  Future<UserEntity> call({
    required String firstName,
    String? lastName,
    required String email,
    required String password,
  }) async {
    if (firstName.isEmpty || email.isEmpty || password.isEmpty) {
      throw ArgumentError('First name, email and password are required');
    }

    if (password.length < 6) {
      throw ArgumentError("Password need to be bigger than 6 characters");
    }

    return await repository.getUserProfileData(
      firstName: firstName,
      lastName: lastName,
      email: email,
      password: password,
    );
  }
}
