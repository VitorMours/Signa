part of 'camera_page_cubit.dart';

abstract class CameraPageState {}

class CameraPageInitial extends CameraPageState {}

class CameraPageLoading extends CameraPageState {}

class CameraPageReady extends CameraPageState {
  final CameraController controller;
  CameraPageReady(this.controller);
}

class CameraPageError extends CameraPageState {
  final String message;
  CameraPageError(this.message);
}

class CameraPageStreaming extends CameraPageState {
  final CameraController controller;
  CameraPageStreaming(this.controller);
}
