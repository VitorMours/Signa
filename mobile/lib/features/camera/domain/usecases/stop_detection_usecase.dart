import 'package:mobile/features/camera/domain/interfaces/detection_repository_interface.dart';

class StopDetectionStream {
  final DetectionRepositoryInterface _repository;

  StopDetectionStream(this._repository);

  Future<void> call() => _repository.disconnect();
}
