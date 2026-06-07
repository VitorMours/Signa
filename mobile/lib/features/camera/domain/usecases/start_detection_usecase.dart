import 'dart:typed_data';

import 'package:mobile/features/camera/domain/entities/hands_entities.dart';
import 'package:mobile/features/camera/domain/entities/head_entities.dart';
import 'package:mobile/features/camera/domain/entities/pose_entities.dart';
import 'package:mobile/features/camera/domain/interfaces/detection_repository_interface.dart';

class StartDetectionStream {
  final DetectionRepositoryInterface _repository;

  StartDetectionStream(this._repository);

  Future<void> call() => _repository.connect();

  void sendFrame(Uint8List bytes) => _repository.sendFrame(bytes);

  Stream<HandEntity> get handStream => _repository.handStream;
  Stream<BodyEntity> get bodyStream => _repository.bodyStream;
  Stream<HeadEntity> get headStream => _repository.headStream;
}
