part of 'login_page_cubit.dart';

@immutable
sealed class LoginPageEvent extends Equatable {
  const LoginPageEvent();

  @override
  List<Object?> get props => [];
}

class LoginEmailChanged extends LoginPageEvent {
  const LoginEmailChanged(this.email);
  final String email;
}

class LoginPasswordChanged extends LoginPageEvent {
  const LoginPasswordChanged(this.password);
  final String password;
}

final class LoginSubmitted extends LoginPageEvent {
  const LoginSubmitted();
}
