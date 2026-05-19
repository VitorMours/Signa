import 'package:flutter/material.dart';
import 'package:mobile/core/components/form_input.dart';
import 'package:gap/gap.dart';
import 'package:go_router/go_router.dart';
import 'package:mobile/core/components/wave_clipper.dart';

import '../../../../../utils/theme.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  _LoginPageState createState() {
    return _LoginPageState();
  }
}

class _LoginPageState extends State<LoginPage> {
  final _loginFormKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.surface,
      resizeToAvoidBottomInset: true,
      body: Stack(
        children: [
          // Gradient background
          Container(
            height: 320,
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                colors: [Color(0xFF5B21FF), Color(0xFF00C2FF)],
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
              ),
            ),
          ),

          // Wave effect
          ClipPath(
            clipper: WaveClipper(),
            child: Container(height: 360, color: AppColors.surface),
          ),

          // Content
          SafeArea(
            child: Column(
              children: [
                const SizedBox(height: 210),

                // Fixed logo
                Center(child: Text("Signa", style: AppTextStyle.logoTextStyle)),

                const SizedBox(height: 50),

                // Scrollable form
                Expanded(
                  child: SingleChildScrollView(
                    keyboardDismissBehavior:
                        ScrollViewKeyboardDismissBehavior.onDrag,
                    padding: const EdgeInsets.all(24),
                    child: Form(
                      key: _loginFormKey,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          FormInput(
                            validator: (String? value) {
                              if (value == null || value.trim().isEmpty) {
                                return "Por favor, coloque um email correto";
                              }
                              return null;
                            },
                            labelText: 'Email',
                            hintText: 'Enter your email',
                          ),

                          const Gap(24),

                          FormInput(
                            validator: (String? value) {
                              if (value == null || value.trim().isEmpty) {
                                return "Please input text";
                              }
                              return null;
                            },
                            labelText: 'Senha',
                            hintText: 'Coloque a sua senha',
                          ),

                          Align(
                            alignment: Alignment.centerRight,
                            child: TextButton(
                              onPressed: () => context.go('/signin'),
                              child: const Text("Não possui conta?"),
                            ),
                          ),

                          const Gap(42),

                          Center(
                            child: ElevatedButton(
                              onPressed: () {
                                if (_loginFormKey.currentState!.validate()) {
                                  // Perform login action
                                }
                              },
                              child: const Text("Login"),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
