import 'package:get_it/get_it.dart';
import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/core/networks/http_client.dart';
import 'package:mobile/core/services/auth_token_service.dart';

import 'package:mobile/features/auth/login/data/datasource/login_datasource.dart';
import 'package:mobile/features/auth/login/data/repositories/login_repository_impl.dart';
import 'package:mobile/features/auth/login/domain/usecases/login_with_email_use_case.dart';
import 'package:mobile/features/auth/login/presentation/cubits/login_page_cubit.dart';

import 'package:mobile/features/camera/data/datasource/ws_client.dart';
import 'package:mobile/features/camera/data/repositories/detection_repository_impl.dart';
import 'package:mobile/features/camera/domain/interfaces/detection_repository_interface.dart';
import 'package:mobile/features/camera/domain/usecases/start_detection_usecase.dart';
import 'package:mobile/features/camera/domain/usecases/stop_detection_usecase.dart';

import 'package:mobile/features/profile/data/datasources/profile_datasource.dart';
import 'package:mobile/features/profile/data/repositories/profile_repository_interface_impl.dart';
import 'package:mobile/features/profile/domain/usecases/get_profile_data_usecase.dart';
import 'package:mobile/features/profile/presentation/cubits/profile_page_cubit.dart';

final sl = GetIt.instance;

Future<void> initDependencies() async {
  // ---------------------------------------------------------------------------
  // 1. Core
  // ---------------------------------------------------------------------------
  sl.registerLazySingleton<AppLogger>(() => AppLogger());
  sl.registerLazySingleton<AuthTokenService>(() => AuthTokenService());
  sl.registerLazySingleton<HttpClient>(
    () => HttpClient(sl<AuthTokenService>()),
  );

  // ---------------------------------------------------------------------------
  // 2. Auth
  // ---------------------------------------------------------------------------
  sl.registerLazySingleton<LoginDataSource>(
    () => LoginDataSource(sl<HttpClient>()),
  );
  sl.registerLazySingleton<LoginRepositoryImpl>(
    () => LoginRepositoryImpl(sl()),
  );
  sl.registerLazySingleton<LoginWithEmailUseCase>(
    () => LoginWithEmailUseCase(sl()),
  );
  sl.registerFactory(() => LoginPageBloc(loginWithEmailUseCase: sl()));

  // ---------------------------------------------------------------------------
  // 3. Camera
  // ---------------------------------------------------------------------------
  sl.registerLazySingleton<WsClient>(() => WsClient());
  sl.registerLazySingleton<DetectionRepositoryInterface>(
    () => DetectionRepositoryImpl(sl<WsClient>()),
  );
  sl.registerLazySingleton<StartDetectionStream>(
    () => StartDetectionStream(sl<DetectionRepositoryInterface>()),
  );
  sl.registerLazySingleton<StopDetectionStream>(
    () => StopDetectionStream(sl<DetectionRepositoryInterface>()),
  );

  // ---------------------------------------------------------------------------
  // 4. Profile
  // ---------------------------------------------------------------------------
  sl.registerLazySingleton<ProfileDataSource>(
    () => ProfileDataSource(sl<HttpClient>()),
  );
  sl.registerLazySingleton<ProfileRepositoryInterfaceImpl>(
    () => ProfileRepositoryInterfaceImpl(sl<ProfileDataSource>()),
  );
  sl.registerLazySingleton<GetProfileDataUseCase>(
    () => GetProfileDataUseCase(sl<ProfileRepositoryInterfaceImpl>()),
  );
  sl.registerFactory<ProfilePageCubit>(
    () => ProfilePageCubit(sl<GetProfileDataUseCase>()),
  );
}
