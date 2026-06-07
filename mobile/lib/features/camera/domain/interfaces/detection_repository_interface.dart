import 'dart:async';
import 'dart:typed_data';

import 'package:mobile/features/camera/domain/entities/hands_entities.dart';
import 'package:mobile/features/camera/domain/entities/head_entities.dart';
import 'package:mobile/features/camera/domain/entities/pose_entities.dart';

abstract class DetectionRepositoryInterface {
  Future<void> connect();
  Future<void> disconnect();

  Stream<BodyEntity> get bodyStream;
  Stream<HandEntity> get handStream;
  Stream<HeadEntity> get headStream;

  void sendFrame(Uint8List bytes);
}
