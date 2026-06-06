import "package:flutter/material.dart";
import "package:flutter_bloc/flutter_bloc.dart";
import "package:camera/camera.dart";
import "package:mobile/features/camera/presentation/widgets/hand_painter.dart";
import "../cubits/camera_page_cubit.dart";

class CameraPage extends StatelessWidget {
  const CameraPage({super.key});

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (context) => CameraPageCubit()..initCamera(),
      child: const _CameraView(),
    );
  }
}

class _CameraView extends StatelessWidget {
  const _CameraView();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: BlocListener<CameraPageCubit, CameraPageState>(
        listener: (context, state) {
          if (state is CameraPageError) {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                content: Text(state.message),
                backgroundColor: Colors.red,
              ),
            );
          }
        },
        child: BlocBuilder<CameraPageCubit, CameraPageState>(
          builder: (context, state) {
            if (state is CameraPageLoading) {
              return const Center(child: CircularProgressIndicator());
            }

            if (state is CameraPageReady) {
              return _PageLayout(
                cameraContent: Stack(
                  children: [
                    SizedBox.expand(child: CameraPreview(state.controller)),
                  ],
                ),
                button: _RecordButton(
                  onTap: () => context.read<CameraPageCubit>().startStreaming(),
                  isStreaming: false,
                ),
              );
            }

            if (state is CameraPageStreaming) {
              final gestureData = state.lastResult?['gesture'];
              final hands = _parseHands(
                gestureData is Map ? gestureData['hands'] : null,
              );
              final previewSize = state.controller.value.previewSize;
              final isFront =
                  state.controller.description.lensDirection ==
                  CameraLensDirection.front;

              return _PageLayout(
                cameraContent: Stack(
                  children: [
                    SizedBox.expand(child: CameraPreview(state.controller)),
                    Positioned.fill(
                      child: CustomPaint(
                        painter: HandLandmarksPainter(
                          hands,
                          previewSize: previewSize,
                          isMirrored: isFront,
                        ),
                      ),
                    ),
                    // Badge AO VIVO
                    Positioned(
                      top: 12,
                      left: 12,
                      child: Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 10,
                          vertical: 5,
                        ),
                        decoration: BoxDecoration(
                          color: Colors.red,
                          borderRadius: BorderRadius.circular(20),
                        ),
                        child: const Row(
                          children: [
                            Icon(Icons.circle, color: Colors.white, size: 8),
                            SizedBox(width: 5),
                            Text(
                              'AO VIVO',
                              style: TextStyle(
                                color: Colors.white,
                                fontWeight: FontWeight.bold,
                                fontSize: 11,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
                button: _RecordButton(
                  onTap: () => context.read<CameraPageCubit>().stopStreaming(),
                  isStreaming: true,
                ),
              );
            }

            if (state is CameraPageError) {
              return Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Icon(
                      Icons.error_outline,
                      size: 64,
                      color: Colors.red,
                    ),
                    const SizedBox(height: 16),
                    Text(state.message),
                    const SizedBox(height: 16),
                    ElevatedButton(
                      onPressed: () =>
                          context.read<CameraPageCubit>().initCamera(),
                      child: const Text('Tentar novamente'),
                    ),
                  ],
                ),
              );
            }

            return const SizedBox.shrink();
          },
        ),
      ),
    );
  }

  List<List<Map<String, dynamic>>> _parseHands(dynamic rawHands) {
    if (rawHands is List) {
      return rawHands
          .map<List<Map<String, dynamic>>>((hand) {
            if (hand is List) {
              return hand
                  .map<Map<String, dynamic>>((landmark) {
                    if (landmark is Map)
                      return Map<String, dynamic>.from(landmark);
                    return <String, dynamic>{};
                  })
                  .where((l) => l.containsKey('x') && l.containsKey('y'))
                  .toList();
            }
            if (hand is Map) {
              final l = Map<String, dynamic>.from(hand);
              if (l.containsKey('x') && l.containsKey('y')) return [l];
            }
            return <Map<String, dynamic>>[];
          })
          .where((hand) => hand.isNotEmpty)
          .toList();
    }
    return [];
  }
}

class _PageLayout extends StatelessWidget {
  final Widget cameraContent;
  final Widget button;

  const _PageLayout({required this.cameraContent, required this.button});

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 24),
        child: Column(
          children: [
            // Container da câmera
            Expanded(
              child: Container(
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(24),
                  color: Colors.black,
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withOpacity(0.15),
                      blurRadius: 16,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                clipBehavior: Clip.hardEdge,
                child: cameraContent,
              ),
            ),
            const SizedBox(height: 32),
            button,
            const SizedBox(height: 16),
          ],
        ),
      ),
    );
  }
}

class _RecordButton extends StatelessWidget {
  final VoidCallback onTap;
  final bool isStreaming;

  const _RecordButton({required this.onTap, required this.isStreaming});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        width: 72,
        height: 72,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          color: isStreaming ? Colors.red : Colors.black,
          border: Border.all(
            color: isStreaming ? Colors.red.shade200 : Colors.black26,
            width: 4,
          ),
        ),
        child: Icon(
          isStreaming ? Icons.stop : Icons.videocam,
          color: Colors.white,
          size: 32,
        ),
      ),
    );
  }
}
