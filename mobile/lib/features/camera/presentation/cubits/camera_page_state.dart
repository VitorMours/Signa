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
  final HandEntity? handEntity;
  final BodyEntity? bodyEntity;
  final HeadEntity? headEntity;

  CameraPageStreaming(
    this.controller, {
    this.handEntity,
    this.bodyEntity,
    this.headEntity,
  });

  CameraPageStreaming copyWith({
    HandEntity? handEntity,
    BodyEntity? bodyEntity,
    HeadEntity? headEntity,
  }) {
    return CameraPageStreaming(
      controller,
      handEntity: handEntity ?? this.handEntity,
      bodyEntity: bodyEntity ?? this.bodyEntity,
      headEntity: headEntity ?? this.headEntity,
    );
  }
}
