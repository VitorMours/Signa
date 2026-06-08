import 'package:web_socket/web_socket.dart';

class WsClient {
  Future<List<WebSocket>> createSockets() async {
    String host = "10.56.250.245";
    final hand_socket = await WebSocket.connect(
      Uri.parse("ws://$host:8080/v1/gesture-detection/process"),
    );
    final body_socket = await WebSocket.connect(
      Uri.parse("ws://$host:8081/v1/posture-detection/process"),
    );
    final head_socket = await WebSocket.connect(
      Uri.parse("ws://$host:8082/v1/head-detection/process"),
    );

    return [hand_socket, body_socket, head_socket];
  }
}
