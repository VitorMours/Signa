import "package:flutter/material.dart";
import "package:flutter_bloc/flutter_bloc.dart";
import "package:camera/camera.dart";
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
      backgroundColor: Colors.black,
      body: BlocListener<CameraPageCubit, CameraPageState>(
        listener: (context, state) {
          // ✅ sem arrow, sem chaves de Set
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
              return const Center(
                child: CircularProgressIndicator(color: Colors.white),
              );
            }

            if (state is CameraPageReady) {
              return Stack(
                children: [
                  // Preview da câmera
                  SizedBox.expand(child: CameraPreview(state.controller)),
                  // Botão de iniciar stream
                  Positioned(
                    bottom: 48,
                    left: 0,
                    right: 0,
                    child: Center(
                      child: GestureDetector(
                        onTap: () =>
                            context.read<CameraPageCubit>().startStreaming(),
                        child: Container(
                          width: 72,
                          height: 72,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: Colors.white,
                            border: Border.all(color: Colors.white, width: 4),
                          ),
                          child: const Icon(
                            Icons.videocam,
                            color: Colors.black,
                            size: 32,
                          ),
                        ),
                      ),
                    ),
                  ),
                ],
              );
            }

            if (state is CameraPageStreaming) {
              return Stack(
                children: [
                  // Preview da câmera
                  SizedBox.expand(child: CameraPreview(state.controller)),
                  // Badge AO VIVO
                  Positioned(
                    top: 48,
                    left: 16,
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 12,
                        vertical: 6,
                      ),
                      decoration: BoxDecoration(
                        color: Colors.red,
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: const Row(
                        children: [
                          Icon(Icons.circle, color: Colors.white, size: 10),
                          SizedBox(width: 6),
                          Text(
                            'AO VIVO',
                            style: TextStyle(
                              color: Colors.white,
                              fontWeight: FontWeight.bold,
                              fontSize: 12,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  // Botão de parar stream
                  Positioned(
                    bottom: 48,
                    left: 0,
                    right: 0,
                    child: Center(
                      child: GestureDetector(
                        onTap: () =>
                            context.read<CameraPageCubit>().stopStreaming(),
                        child: Container(
                          width: 72,
                          height: 72,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: Colors.red,
                            border: Border.all(color: Colors.white, width: 4),
                          ),
                          child: const Icon(
                            Icons.stop,
                            color: Colors.white,
                            size: 32,
                          ),
                        ),
                      ),
                    ),
                  ),
                ],
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
                    Text(
                      state.message,
                      style: const TextStyle(color: Colors.white),
                    ),
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
}
