import 'package:flutter/material.dart';
import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/core/networks/http_client.dart';
import 'package:mobile/core/routes/app_router.dart';
import 'package:mobile/utils/theme.dart';
import "package:flutter_bloc/flutter_bloc.dart";
import 'core/di/injection_container.dart' as di;
import 'core/di/injection_container.dart' show sl;

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await di.initDependencies();

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiRepositoryProvider(
      providers: [
        RepositoryProvider<HttpClient>(
          create: (context) => sl<HttpClient>(),
        ),
        RepositoryProvider<AppLogger>(
          create: (context) => sl<AppLogger>(),
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
