import 'package:flutter/material.dart';
import 'package:mobile/core/routes/app_router.dart';
import 'package:mobile/utils/theme.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(theme: AppTheme.dark, routerConfig: router);
  }
}
