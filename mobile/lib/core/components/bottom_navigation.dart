import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class BottomNavigation extends StatelessWidget {
  const BottomNavigation({super.key});

  // Lê a URL atual para decidir qual ícone destacar
  int _calculateSelectedIndex(BuildContext context) {
    final String location = GoRouterState.of(context).uri.path;
    if (location == '/home') return 0;
    if (location == '/camera') return 1;
    if (location == '/notes') return 2;
    if (location == '/profile') return 3;
    return 0;
  }

  @override
  Widget build(BuildContext context) {
    return NavigationBar(
      selectedIndex: _calculateSelectedIndex(context),
      onDestinationSelected: (int index) {
        switch (index) {
          case 0:
            context.go('/home');
            break;
          case 1:
            context.go('/camera');
            break;
          case 2:
            context.go('/notes');
            break;
          case 3:
            context.go('/profile');
            break;
        }
      },
      destinations: const [
        NavigationDestination(icon: Icon(Icons.home), label: ''),
        NavigationDestination(icon: Icon(Icons.camera_alt), label: ''),
        NavigationDestination(icon: Icon(Icons.book), label: ''),
        NavigationDestination(icon: Icon(Icons.person), label: ''),
      ],
    );
  }
}
