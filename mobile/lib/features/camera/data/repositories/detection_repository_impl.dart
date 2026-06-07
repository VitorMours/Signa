import 'dart:typed_data';

import 'package:mobile/features/camera/data/datasource/ws_client.dart';
import 'package:mobile/features/camera/domain/entities/hands_entities.dart';
import 'package:mobile/features/camera/domain/entities/head_entities.dart';
import 'package:mobile/features/camera/domain/entities/pose_entities.dart';
import 'package:mobile/features/camera/domain/interfaces/detection_repository_interface.dart';

class DetectionRepositoryImpl implements DetectionRepositoryInterface {
  final WsClient _wsClient;

  DetectionRepositoryImpl(this._wsClient);

  @override
  Stream<BodyEntity> get bodyStream => _wsClient.bodyStream.map((json) {
    final postureData = json['posture'];
    if (postureData == null) {
      return BodyEntity(success: false, landmarks: []);
    }
    return BodyEntity(
      success: postureData['success'] as bool? ?? false,
      landmarks: _parseLandmarks(
        postureData['poses']?[0],
      ), // pega a primeira pose
      posture: postureData['posture']?.toString(),
    );
  });

  @override
  Stream<HandEntity> get handStream => _wsClient.handStream.map((json) {
    final gestureData = json['gesture'];

    if (gestureData == null) {
      return HandEntity(success: true, hands: []);
    }

    return HandEntity(
      success: gestureData['success'] as bool? ?? false,
      hands: _parseHands(gestureData['hands']),
      gesture: gestureData['gesture']?.toString(),
    );
  });

  @override
  Stream<HeadEntity> get headStream => _wsClient.headStream.map((json) {
    final gestureData = json['gesture'];
    if (gestureData == null) {
      return HeadEntity(success: false, faces: []);
    }
    return HeadEntity(
      success: gestureData['success'] as bool? ?? false,
      faces: _parseFaces(gestureData['faces']),
      orientation: gestureData['orientation']?.toString(),
    );
  });
  List<List<Map<String, double>>> _parseHands(dynamic raw) {
    if (raw is! List) return [];
    return raw.map<List<Map<String, double>>>((hand) {
      if (hand is! List) return [];
      return hand.map<Map<String, double>>((landmark) {
        if (landmark is! Map) return {};
        return {
          'x': _toDouble(landmark['x']),
          'y': _toDouble(landmark['y']),
          'z': _toDouble(landmark['z']),
        };
      }).toList();
    }).toList();
  }

  List<Map<String, double>> _parseLandmarks(dynamic raw) {
    if (raw is! List) return [];
    return raw.map<Map<String, double>>((landmark) {
      if (landmark is! Map) return {};
      return {
        'x': _toDouble(landmark['x']),
        'y': _toDouble(landmark['y']),
        'z': _toDouble(landmark['z']),
        'visibility': _toDouble(landmark['visibility']),
      };
    }).toList();
  }

  List<List<Map<String, double>>> _parseFaces(dynamic raw) {
    if (raw is! List) return [];
    return raw.map<List<Map<String, double>>>((face) {
      if (face is! List) return [];
      return face.map<Map<String, double>>((landmark) {
        if (landmark is! Map) return {};
        return {
          'x': _toDouble(landmark['x']),
          'y': _toDouble(landmark['y']),
          'z': _toDouble(landmark['z']),
        };
      }).toList();
    }).toList();
  }

  double _toDouble(dynamic value) {
    if (value is double) return value;
    if (value is int) return value.toDouble();
    if (value is String) return double.tryParse(value) ?? 0.0;
    return 0.0;
  }

  @override
  void sendFrame(Uint8List bytes) => _wsClient.sendFrame(bytes);

  @override
  Future<void> disconnect() => _wsClient.disconnect();

  @override
  Future<void> connect() => _wsClient.connect();
}
