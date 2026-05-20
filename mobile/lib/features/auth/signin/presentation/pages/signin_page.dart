import 'package:flutter/material.dart';
import 'package:mobile/core/components/form_input.dart';
import 'package:gap/gap.dart';
import 'package:go_router/go_router.dart';
import 'package:mobile/core/components/wave_clipper.dart';

import '../../../../../utils/theme.dart';

class SigninPage extends StatefulWidget {
  const SigninPage({super.key});

  @override
  SigninPageState createState() {
    return SigninPageState();
  }
}

class SigninPageState extends State<SigninPage> {
  final _signinFormKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.surface,
      resizeToAvoidBottomInset: true,
      body: Stack(
        children: [
          Container(
            height: 340,
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                colors: [Color(0xFF5B21FF), Color(0xFF00C2FF)],
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
              ),
            ),
          ),
          ClipPath(
            clipper: WaveClipper(),
            child: Container(height: 480, color: AppColors.surface),
          ),
          SafeArea(
            child: LayoutBuilder(
              builder: (context, constraints) {
                return SingleChildScrollView(
                  keyboardDismissBehavior:
                      ScrollViewKeyboardDismissBehavior.onDrag,
                  child: ConstrainedBox(
                    constraints: BoxConstraints(
                      minHeight: constraints.maxHeight,
                    ),
                    child: IntrinsicHeight(
                      child: Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 24.0),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.stretch,
                          children: [
                            const Gap(160),
                            const Spacer(flex: 2),
                            Center(
                              child: Text(
                                'Signa',
                                style: AppTextStyle.logoTextStyle,
                              ),
                            ),
                            const Spacer(flex: 1),
                            Form(
                              key: _signinFormKey,
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Row(
                                    children: [
                                      Expanded(
                                        child: FormInput(
                                          validator: (String? value) {
                                            if (value == null ||
                                                value.trim().isEmpty) {
                                              return 'Por favor, informe seu nome';
                                            }
                                            return null;
                                          },
                                          labelText: 'Nome',
                                          hintText: 'John',
                                        ),
                                      ),
                                      const Gap(16),
                                      Expanded(
                                        child: FormInput(
                                          validator: (String? value) {
                                            if (value == null ||
                                                value.trim().isEmpty) {
                                              return 'Por favor, informe seu sobrenome';
                                            }
                                            return null;
                                          },
                                          labelText: 'Sobrenome',
                                          hintText: 'Doe',
                                        ),
                                      ),
                                    ],
                                  ),
                                  const Gap(20),
                                  FormInput(
                                    validator: (String? value) {
                                      if (value == null ||
                                          value.trim().isEmpty) {
                                        return 'Por favor, coloque um email correto';
                                      }
                                      return null;
                                    },
                                    labelText: 'Email',
                                    hintText: 'Digite seu Email',
                                  ),
                                  const Gap(20),
                                  FormInput(
                                    validator: (String? value) {
                                      if (value == null ||
                                          value.trim().isEmpty) {
                                        return 'Por favor, coloque uma senha';
                                      }
                                      return null;
                                    },
                                    labelText: 'Senha',
                                    hintText: 'Digite sua senha',
                                  ),
                                  const Gap(20),
                                  FormInput(
                                    validator: (String? value) {
                                      if (value == null ||
                                          value.trim().isEmpty) {
                                        return 'Por favor, repita a senha';
                                      }
                                      return null;
                                    },
                                    labelText: 'Repita sua Senha',
                                    hintText: 'Digite a senha de novo',
                                  ),
                                  const Gap(8),
                                  Align(
                                    alignment: Alignment.centerRight,
                                    child: TextButton(
                                      onPressed: () => context.go('/login'),
                                      child: const Text('Já possui conta?'),
                                    ),
                                  ),
                                  const Gap(32),
                                  Center(
                                    child: ElevatedButton(
                                      onPressed: () {
                                        if (_signinFormKey.currentState!
                                            .validate()) {
                                          // Ação de criação de conta
                                        }
                                      },
                                      child: const Text('Criar Conta'),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            const Spacer(flex: 1),
                          ],
                        ),
                      ),
                    ),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
