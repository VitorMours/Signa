import 'dart:io';
import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/core/networks/http_client.dart';
import 'package:mobile/core/routes/app_router.dart';
import 'package:mobile/core/services/auth_token_service.dart';
import 'package:mobile/utils/theme.dart';
import "package:flutter_bloc/flutter_bloc.dart";
import "package:path_provider/path_provider.dart";
import 'core/di/injection_container.dart' as di;
import 'core/di/injection_container.dart' show sl;

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  final appDocumentDir = await getApplicationDocumentsDirectory();
  final hiveDirectory = Directory('${appDocumentDir.path}/hive_data');
  
  if (!hiveDirectory.existsSync()) {
    hiveDirectory.createSync(recursive: true);
  }
  
  Hive.init(hiveDirectory.path);
  await di.initDependencies();
  // await sl<AuthTokenService>().initDependencies();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiRepositoryProvider(
      providers: [
        RepositoryProvider<HttpClient>(create: (context) => sl<HttpClient>()),
        RepositoryProvider<AppLogger>(create: (context) => sl<AppLogger>()),
        RepositoryProvider<AuthTokenService>(
          create: (context) => sl<AuthTokenService>(),
        ),
      ],
      child: MaterialApp.router(
        theme: AppTheme.dark,
        routerConfig: router,
        debugShowCheckedModeBanner: false,
      ),
    );
  }
}
