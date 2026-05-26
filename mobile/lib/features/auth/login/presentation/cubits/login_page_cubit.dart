import 'package:dio/dio.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/foundation.dart';
import 'package:mobile/core/components/app_logger.dart';
import 'package:mobile/features/auth/login/domain/usecases/login_with_email_use_case.dart';

part 'login_page_state.dart';
part 'login_page_event.dart';

class LoginPageBloc extends Bloc<LoginPageEvent, LoginState> {
  // 1. Declare o UseCase como uma dependência final
  final LoginWithEmailUseCase _loginWithEmailUseCase;

  // 2. Peça o UseCase no construtor do Bloc
  LoginPageBloc({required LoginWithEmailUseCase loginWithEmailUseCase})
    : _loginWithEmailUseCase = loginWithEmailUseCase,
      super(const LoginState()) {
    on<LoginEmailChanged>(_onEmailChanged);
    on<LoginPasswordChanged>(_onPasswordChanged);
    on<LoginSubmitted>(_onSubmitted);
  }

  String _returnErrorMessage(DioException error) {
    final statusCode = error.response?.statusCode;

    // Mensagem customizada para 401 Unauthorized
    switch (statusCode) {
      case 401:
        return 'Credenciais inválidas. Verifique seu email e senha.';
      case 200:
        final data = error.response?.data;
        if (data is Map) {
          final detail = data['detail'] ?? data['message'] ?? data['error'];
          if (detail is String && detail.isNotEmpty) {
            if (detail.toLowerCase().contains('invalid') ||
                detail.toLowerCase().contains('credentials')) {
              return 'Email ou senha inválidos';
            }
            return detail;
          }
        }
      default:
        return "Ocorreu um erro nao identificado no login";
    }
    return 'Erro ao fazer login';
  }

  void _onEmailChanged(LoginEmailChanged event, Emitter<LoginState> emit) {
    emit(state.copyWith(email: event.email));
  }

  void _onPasswordChanged(
    LoginPasswordChanged event,
    Emitter<LoginState> emit,
  ) {
    emit(state.copyWith(password: event.password));
  }

  void _onSubmitted(LoginSubmitted event, Emitter<LoginState> emit) async {
    if (state.status == LoginStatus.loading) return;

    emit(state.copyWith(status: LoginStatus.loading));

    try {
      final user = await _loginWithEmailUseCase(
        email: state.email,
        password: state.password,
      );
      AppLogger.i('Executando login do usuario $user');
      emit(state.copyWith(status: LoginStatus.success));
    } on DioException catch (e, _) {
      emit(
        state.copyWith(
          status: LoginStatus.failure,
          errorMessage: _returnErrorMessage(e),
        ),
      );
    }
  }
}
