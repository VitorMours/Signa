import 'package:equatable/equatable.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:mobile/core/entities/user_entity.dart';
import 'package:mobile/features/profile/domain/usecases/get_profile_data_usecase.dart';

part 'profile_page_state.dart';

class ProfilePageCubit extends Cubit<ProfilePageState> {
  final GetProfileDataUseCase profileUseCase;
  ProfilePageCubit(this.profileUseCase) : super(ProfilePageInitial());

  Future<void> loadProfile() async {
    emit(ProfilePageLoading());
    try {
      final response = await this.profileUseCase.call();
      emit(ProfilePageSuccess(response));
    } catch (e) {
      emit(ProfilePageFailure());
    }
  }
}
