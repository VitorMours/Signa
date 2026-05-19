import 'package:go_router/go_router.dart';
import 'package:mobile/core/routes/routes_names.dart';
import 'package:mobile/features/auth/login/presentation/pages/login_page.dart';

import '../../features/auth/signin/presentation/pages/signin_page.dart';

final router = GoRouter(
  initialLocation: Routes.login,
  routes: [
    GoRoute(path: Routes.login, builder: (context, state) => LoginPage()),
    GoRoute(path: Routes.signin, builder: (context, state) => SigninPage()),
    // GoRoute(path: Routes.splash, builder: (context, state) => SplashPage()),
  ],
);
