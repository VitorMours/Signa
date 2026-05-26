part of 'login_page_cubit.dart';

enum LoginStatus { initial, loading, success, failure }

final class LoginState extends Equatable {
  const LoginState({
    this.status = LoginStatus.initial,
    this.email = 'email',
    this.password = 'password',
    this.errorMessage,
  });

  final LoginStatus status;
  final String email;
  final String password;
  final String? errorMessage;

  static final _emailRegex = RegExp(r'^[\w.-]+@[\w-]+\.[a-zA-Z]{2,}$');
  bool get isEmailValid => _emailRegex.hasMatch(email);

  bool get isPasswordValid =>
      password.length >= 8 &&
      password.contains(RegExp(r'[A-Z]')) &&
      password.contains(RegExp(r'[0-9]'));

  bool get isValid => isEmailValid && isPasswordValid;
  LoginState copyWith({
    LoginStatus? status,
    String? email,
    String? password,
    String? errorMessage,
  }) => LoginState(
    status: status ?? this.status,
    email: email ?? this.email,
    password: password ?? this.password,
    errorMessage: errorMessage ?? this.errorMessage,
  );

  @override
  List<Object?> get props => [status, email, password, errorMessage];
}
