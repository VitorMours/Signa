import "package:flutter/material.dart";
import "package:mobile/core/components/form_input.dart";
import "package:gap/gap.dart";
import "package:mobile/core/di/injection_container.dart";
import "package:mobile/features/profile/presentation/cubits/profile_page_cubit.dart";
import "package:flutter_bloc/flutter_bloc.dart";

class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (context) => sl<ProfilePageCubit>()..loadProfile(),
      child: _ProfileView(),
    );
  }
}

// 👇 Mudou para StatefulWidget por causa do formKey
class _ProfileView extends StatefulWidget {
  const _ProfileView();

  @override
  State<_ProfileView> createState() => _ProfileViewState();
}

class _ProfileViewState extends State<_ProfileView> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: BlocListener<ProfilePageCubit, ProfilePageState>(
        listener: (BuildContext context, ProfilePageState state) {
          if (state is ProfilePageFailure) {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                content: const Text('Erro ao carregar perfil!'),
                backgroundColor: Colors.red,
                action: SnackBarAction(
                  label: 'Tentar novamente',
                  textColor: Colors.white,
                  onPressed: () =>
                      context.read<ProfilePageCubit>().loadProfile(),
                ),
              ),
            );
          }
        },
        child: BlocBuilder<ProfilePageCubit, ProfilePageState>(
          builder: (context, state) {
            if (state is ProfilePageLoading) {
              return const Center(child: CircularProgressIndicator());
            }

            if (state is ProfilePageSuccess) {
              return Padding(
                padding: const EdgeInsets.symmetric(horizontal: 24.0),
                child: Column(
                  children: <Widget>[
                    Text("Informacoes Pessoais"),
                    Column(
                      children: <Widget>[
                        Row(
                          children: <Widget>[
                            Expanded(
                              child: Column(children: [Text("Primeiro Nome")]),
                            ),
                            Gap(16),
                            Expanded(child: Text("das")),
                          ],
                        ),
                        Text("asd"),
                        Text("asd"),
                      ],
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
