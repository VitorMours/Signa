import 'dart:async';
import 'dart:convert';
import 'dart:typed_data';

import 'package:web_socket/web_socket.dart';

class WsClient {
  static const String _host = '10.56.250.245';

  WebSocket? _handSocket;
  WebSocket? _bodySocket;
  WebSocket? _headSocket;

  StreamController<Map<String, dynamic>> _handController =
      StreamController<Map<String, dynamic>>.broadcast();
  StreamController<Map<String, dynamic>> _bodyController =
      StreamController<Map<String, dynamic>>.broadcast();
  StreamController<Map<String, dynamic>> _headController =
      StreamController<Map<String, dynamic>>.broadcast();

  Stream<Map<String, dynamic>> get handStream => _handController.stream;
  Stream<Map<String, dynamic>> get bodyStream => _bodyController.stream;
  Stream<Map<String, dynamic>> get headStream => _headController.stream;

  Future<void> connect() async {
    if (_handController.isClosed) {
      _handController = StreamController<Map<String, dynamic>>.broadcast();
    }
    if (_bodyController.isClosed) {
      _bodyController = StreamController<Map<String, dynamic>>.broadcast();
    }
    if (_headController.isClosed) {
      _headController = StreamController<Map<String, dynamic>>.broadcast();
    }

    _handSocket = await WebSocket.connect(
      Uri.parse('ws://$_host:8080/v1/gesture-detection/process'),
    );
    _bodySocket = await WebSocket.connect(
      Uri.parse('ws://$_host:8081/v1/posture-detection/process'),
    );
    _headSocket = await WebSocket.connect(
      Uri.parse('ws://$_host:8082/v1/head-detection/process'),
    );

    _handSocket!.events.listen(
      (event) {
        if (event is TextDataReceived) {
          final json = jsonDecode(event.text) as Map<String, dynamic>;
          _handController.add(json);
        }
      },
      onError: (error) => _handController.addError(error),
      onDone: () => _handController.close(),
    );

    _bodySocket!.events.listen(
      (event) {
        if (event is TextDataReceived) {
          final json = jsonDecode(event.text) as Map<String, dynamic>;
          _bodyController.add(json);
        }
      },
      onError: (error) => _bodyController.addError(error),
      onDone: () => _bodyController.close(),
    );

    _headSocket!.events.listen(
      (event) {
        if (event is TextDataReceived) {
          final json = jsonDecode(event.text) as Map<String, dynamic>;
          _headController.add(json);
        }
      },
      onError: (error) => _headController.addError(error),
      onDone: () => _headController.close(),
    );
  }

  void sendFrame(Uint8List bytes) {
    _handSocket?.sendBytes(bytes);
    _bodySocket?.sendBytes(bytes);
    _headSocket?.sendBytes(bytes);
  }

  Future<void> disconnect() async {
    await _handSocket?.close();
    await _bodySocket?.close();
    await _headSocket?.close();

    if (!_handController.isClosed) await _handController.close();
    if (!_bodyController.isClosed) await _bodyController.close();
    if (!_headController.isClosed) await _headController.close();

    _handSocket = null;
    _bodySocket = null;
    _headSocket = null;
  }
}
