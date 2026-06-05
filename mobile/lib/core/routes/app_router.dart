import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:mobile/core/components/bottom_navigation.dart';
import 'package:mobile/core/routes/routes_names.dart';
import 'package:mobile/features/auth/login/presentation/pages/login_page.dart';
import 'package:mobile/features/camera/presentation/pages/camera_page.dart';
import 'package:mobile/features/notes/presentation/pages/notes_page.dart';
import 'package:mobile/features/profile/presentation/pages/profile_page.dart';
import '../../features/auth/signin/presentation/pages/signin_page.dart';
import '../../features/home/presentation/pages/home_page.dart';

final router = GoRouter(
  initialLocation: Routes.login,
  routes: [
    GoRoute(path: Routes.login, builder: (context, state) => LoginPage()),
    GoRoute(path: Routes.signin, builder: (context, state) => SigninPage()),

    ShellRoute(
      builder: (context, state, child) {
        return Scaffold(body: child, bottomNavigationBar: BottomNavigation());
      },
      routes: [
        GoRoute(path: Routes.home, builder: (context, state) => HomePage()),
        GoRoute(path: Routes.camera, builder: (context, state) => CameraPage()),
        GoRoute(path: Routes.notes, builder: (context, state) => NotesPage()),
        GoRoute(
          path: Routes.profile,
          builder: (context, state) => ProfilePage(),
        ),
      ],
    ),
  ],
);
