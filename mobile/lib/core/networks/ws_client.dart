import 'package:web_socket/web_socket.dart';

class WsClient {
  void createhandSocket() async {
    final hand_socket = await WebSocket.connect(
      Uri.parse("ws://192.168.15.47:8080/v1/gesture-detection/process"),
    );
  }
}
