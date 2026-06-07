import 'dart:io';
import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/core/networks/http_client.dart';
import 'package:mobile/core/routes/app_router.dart';
import 'package:mobile/core/services/auth_token_service.dart';
import 'package:mobile/features/camera/domain/interfaces/detection_repository_interface.dart';
import 'package:mobile/features/camera/domain/usecases/start_detection_usecase.dart';
import 'package:mobile/features/camera/domain/usecases/stop_detection_usecase.dart';
import 'package:mobile/utils/theme.dart';
import "package:flutter_bloc/flutter_bloc.dart";
import "package:path_provider/path_provider.dart";
import 'core/di/injection_container.dart' as di;
import 'core/di/injection_container.dart' show sl;
import 'package:flutter/services.dart'; // Importe necessário para SystemChrome

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  final appDocumentDir = await getApplicationDocumentsDirectory();
  final hiveDirectory = Directory('${appDocumentDir.path}/hive_data');

  if (!hiveDirectory.existsSync()) {
    hiveDirectory.createSync(recursive: true);
  }

  Hive.init(hiveDirectory.path);
  await di.initDependencies();
  await sl<AuthTokenService>().initDependencies();

  SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp]).then((
    _,
  ) {
    runApp(const MyApp());
  });
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiRepositoryProvider(
      providers: [
        // Core
        RepositoryProvider<HttpClient>(create: (_) => sl<HttpClient>()),
        RepositoryProvider<AppLogger>(create: (_) => sl<AppLogger>()),
        RepositoryProvider<AuthTokenService>(
          create: (_) => sl<AuthTokenService>(),
        ),

        // Camera
        RepositoryProvider<DetectionRepositoryInterface>(
          create: (_) => sl<DetectionRepositoryInterface>(),
        ),
        RepositoryProvider<StartDetectionStream>(
          create: (_) => sl<StartDetectionStream>(),
        ),
        RepositoryProvider<StopDetectionStream>(
          create: (_) => sl<StopDetectionStream>(),
        ),
      ],
      child: MaterialApp.router(
        theme: AppTheme.dark,
        routerConfig: router,
        debugShowCheckedModeBanner: true,
      ),
    );
  }
}
