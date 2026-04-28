import 'package:flutter_test/flutter_test.dart';
import 'package:mobile/features/auth/login/domain/entities/auth_user_entity.dart';
import 'package:mobile/features/auth/login/domain/entities/login_entity.dart';
import 'package:mobile/features/auth/login/domain/interfaces/login_repository.dart';
import 'package:mobile/features/auth/login/domain/usecases/login_use_case.dart';
import 'package:mocktail/mocktail.dart';

class MockAuthRepository extends Mock implements LoginRepository {}

void main() {
  late LoginUseCase usecase;
  late MockAuthRepository repository;

  setUp(() {
    repository = MockAuthRepository();
    usecase = LoginUseCase(repository);
  });

  test('VALID: retorna usuario quando o login esta valido', () async {
    when(() => repository.login('email@test.com', '123')).thenAnswer(
      (_) async => AuthUserEntity(
        email: 'email@test.com',
        firstName: 'John',
        lastName: 'Doe',
      ),
    );
    final loginEntity = LoginEntity(email: 'email@test.com', password: '123');

    final result = await usecase(loginEntity);
    expect(result.email, 'email@test.com');
    expect(result.firstName, 'John');
    expect(result.lastName, 'Doe');
    verify(() => repository.login('email@test.com', '123')).called(1);
  });
}
