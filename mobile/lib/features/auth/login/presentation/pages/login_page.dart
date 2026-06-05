import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:mobile/core/components/form_input.dart';
import 'package:gap/gap.dart';
import 'package:go_router/go_router.dart';
import 'package:mobile/core/components/wave_clipper.dart';
import 'package:mobile/features/auth/login/presentation/cubits/login_page_cubit.dart';
import '../../../../../core/di/injection_container.dart';
import '../../../../../utils/theme.dart';

class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (_) => sl<LoginPageBloc>(),
      child: const _LoginView(),
    );
  }
}

class _LoginView extends StatefulWidget {
  const _LoginView();

  @override
  State<_LoginView> createState() => _LoginViewState();
}

class _LoginViewState extends State<_LoginView> {
  final _formKey = GlobalKey<FormState>();

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
        body: LayoutBuilder(
          builder: (context, constraints) {
            return Column(
              children: [
                ClipPath(
                  clipper: WaveClipper(),
                  child:Container(
                      height: 340,
                      decoration: const BoxDecoration(
                        gradient: LinearGradient(
                          colors: [Color(0xFF5B21FF), Color(0xFF00C2FF)],
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
                        ),
                      ),

                  ),
                ),
                Expanded(
                  child: Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 24.0),
                    child: SingleChildScrollView(
                      child: Form(
                        key: _formKey,
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Center(
                              child: Text(
                                "Signa",
                                style: AppTextStyle.logoTextStyle,
                              ),
                            ),

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
                                  validator: (_) {
                                    if (state.email.isEmpty) {
                                      return 'Por favor, informe seu email';
                                    }
                                    if (!state.isEmailValid) {
                                      return 'Email inválido';
                                    }
                                    return null;
                                  },
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
                                  validator: (_) {
                                    if (state.password.isEmpty) {
                                      return 'Por favor, informe sua senha';
                                    }
                                    if (!state.isPasswordValid) {
                                      return 'Senha invalida';
                                    }
                                    return null;
                                  },
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
                                  child: state.status == LoginStatus.loading
                                      ? const CircularProgressIndicator()
                                      : ElevatedButton(
                                          onPressed: () {
                                            final isValid =
                                                _formKey.currentState
                                                    ?.validate() ??
                                                false;
                                            if (!isValid) return;
                                            context.read<LoginPageBloc>().add(
                                              const LoginSubmitted(),
                                            );
                                          },
                                          child: const Text("Login"),
                                        ),
                                );
                              },
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            );
          },
        ),
      ),
    );
  }
}
