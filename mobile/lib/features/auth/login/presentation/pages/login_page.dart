import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:mobile/core/components/form_input.dart';
import 'package:gap/gap.dart';
import 'package:go_router/go_router.dart';
import 'package:mobile/core/components/wave_clipper.dart';
import 'package:mobile/features/auth/login/presentation/cubits/login_page_cubit.dart';

import '../../../../../utils/theme.dart';

class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (_) => LoginPageBloc(),
      child: const _LoginView(),
    );
  }
}

class _LoginView extends StatelessWidget {
  const _LoginView();

  @override
  Widget build(BuildContext context) {
    return BlocListener<LoginPageBloc, LoginState>(
      listenWhen: (prev, curr) => prev.status != curr.status,
      listener: (context, state) {
        if (state.status == LoginStatus.success) {
          context.go('/home');
        }
        if (state.status == LoginStatus.failure) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text(state.errorMessage ?? 'Erro ao fazer login'),
            ),
          );
        }
      },
      child: Scaffold(
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

            // 3. Layout
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
                                  "Signa",
                                  style: AppTextStyle.logoTextStyle,
                                ),
                              ),

                              const Spacer(flex: 1),

                              Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  BlocBuilder<LoginPageBloc, LoginState>(
                                    buildWhen: (prev, curr) =>
                                        prev.email != curr.email,
                                    builder: (context, state) {
                                      return FormInput(
                                        labelText: 'Email',
                                        hintText: 'Enter your email',
                                        onChanged: (value) => context
                                            .read<LoginPageBloc>()
                                            .add(LoginEmailChanged(value)),
                                        validator: (_) =>
                                            null, // validação no BLoC via isValid
                                      );
                                    },
                                  ),

                                  const Gap(20),

                                  // Campo de senha
                                  BlocBuilder<LoginPageBloc, LoginState>(
                                    buildWhen: (prev, curr) =>
                                        prev.password != curr.password,
                                    builder: (context, state) {
                                      return FormInput(
                                        labelText: 'Senha',
                                        hintText: 'Coloque a sua senha',
                                        obscureText: true,
                                        onChanged: (value) => context
                                            .read<LoginPageBloc>()
                                            .add(LoginPasswordChanged(value)),
                                        validator: (_) => null,
                                      );
                                    },
                                  ),

                                  const Gap(8),

                                  Align(
                                    alignment: Alignment.centerRight,
                                    child: TextButton(
                                      onPressed: () => context.go('/signin'),
                                      child: const Text("Não possui conta?"),
                                    ),
                                  ),

                                  const Gap(32),

                                  // Botão de login
                                  BlocBuilder<LoginPageBloc, LoginState>(
                                    buildWhen: (prev, curr) =>
                                        prev.status != curr.status ||
                                        prev.isValid != curr.isValid,
                                    builder: (context, state) {
                                      return Center(
                                        child:
                                            state.status == LoginStatus.loading
                                            ? const CircularProgressIndicator()
                                            : ElevatedButton(
                                                onPressed: state.isValid
                                                    ? () => context
                                                          .read<LoginPageBloc>()
                                                          .add(
                                                            const LoginSubmitted(),
                                                          )
                                                    : null,
                                                child: const Text("Login"),
                                              ),
                                      );
                                    },
                                  ),
                                ],
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
      ),
    );
  }
}
