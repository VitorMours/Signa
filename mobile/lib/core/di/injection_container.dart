import 'package:get_it/get_it.dart';
import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/core/networks/http_client.dart';
import 'package:mobile/core/services/auth_token_service.dart';
import 'package:mobile/features/auth/login/data/datasource/login_datasource.dart';
import 'package:mobile/features/auth/login/data/repositories/login_repository_impl.dart';
import 'package:mobile/features/auth/login/domain/interfaces/login_repository_interface.dart';
import 'package:mobile/features/auth/login/domain/usecases/login_with_email_use_case.dart';
import 'package:mobile/features/auth/login/presentation/cubits/login_page_cubit.dart';

final sl = GetIt.instance;

Future<void> initDependencies() async {
  // ---------------------------------------------------------------------------
  // 1. Adicionando os Bloc's
  // ---------------------------------------------------------------------------
  sl.registerFactory(() => LoginPageBloc(loginWithEmailUseCase: sl()));

  // ---------------------------------------------------------------------------
  // 2. Recursos Externos (Drivers / Core)
  // ---------------------------------------------------------------------------
  sl.registerLazySingleton<HttpClient>(() => HttpClient());
  sl.registerLazySingleton<AppLogger>(() => AppLogger());
  sl.registerLazySingleton<AuthTokenService>(() => AuthTokenService());

  // ---------------------------------------------------------------------------
  // 3. Adicionando os Datasources
  // ---------------------------------------------------------------------------
  sl.registerLazySingleton<LoginDataSource>(
    () => LoginDataSource(sl<HttpClient>()),
  );

  // ---------------------------------------------------------------------------
  // 4. Adicionando os UseCases
  // ---------------------------------------------------------------------------
  sl.registerLazySingleton<LoginWithEmailUseCase>(
    () => LoginWithEmailUseCase(sl()),
  );

  sl.registerLazySingleton<LoginRepositoryImpl>(
    () => LoginRepositoryImpl(sl()),
  );
}
