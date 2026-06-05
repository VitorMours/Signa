part of 'profile_page_cubit.dart';

enum ProfilePageStatus { initial, loading, success, failure }

abstract class ProfilePageState {}

class ProfilePageInitial extends ProfilePageState {
  ProfilePageInitial();
}

class ProfilePageLoading extends ProfilePageState {
  ProfilePageLoading();
}

class ProfilePageSuccess extends ProfilePageState {
  final UserEntity data;
  ProfilePageSuccess(this.data);
}

class ProfilePageFailure extends ProfilePageState {
  ProfilePageFailure();
}
