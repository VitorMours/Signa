import "package:flutter/material.dart";
import "package:mobile/core/components/form_input.dart";
import "package:gap/gap.dart";
import "package:mobile/core/di/injection_container.dart";
import "package:mobile/features/profile/presentation/cubits/profile_page_cubit.dart";
import "package:flutter_bloc/flutter_bloc.dart";
import "package:mobile/utils/theme.dart";

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
              return SingleChildScrollView(
                padding: const EdgeInsets.symmetric(horizontal: 24.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    const Gap(32),

                    Align(
                      alignment: Alignment.center,
                      child: Stack(
                        children: [
                          CircleAvatar(
                            radius: 72,
                            backgroundColor: Colors.grey[300],
                            child: const Icon(Icons.person, size: 72),
                          ),
                          Positioned(
                            bottom: 0,
                            right: 0,
                            child: GestureDetector(
                              onTap: () {}, // abrir galeria
                              child: Container(
                                padding: const EdgeInsets.all(6),
                                decoration: const BoxDecoration(
                                  color: Colors.blue,
                                  shape: BoxShape.circle,
                                ),
                                child: const Icon(
                                  Icons.camera_alt,
                                  size: 18,
                                  color: Colors.white,
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),

                    const Gap(32),

                    Text(
                      "Informações Pessoais",
                      style: AppTextStyle.headingMedium,
                    ),
                    const Gap(16),
                    Row(
                      children: <Widget>[
                        Expanded(
                          child: FormInput(
                            labelText: "Primeiro Nome",
                            hintText: state.data.firstName,
                            validator: (string) {},
                          ),
                        ),
                        const Gap(16),
                        Expanded(
                          child: FormInput(
                            labelText: 'Sobrenome',
                            hintText: state.data.lastName,
                            validator: (String? p1) {},
                          ),
                        ),
                      ],
                    ),
                    const Gap(16),
                    FormInput(
                      labelText: 'Email',
                      hintText: state.data.email,
                      validator: (String? p1) {},
                    ),
                    const Gap(16),
                    FormInput(
                      labelText: 'Bio',
                      hintText: 'Conte-nos mais sobre você...',
                      minLines: 4,
                      maxLines: 6,
                      validator: (String? p1) {},
                    ),
                    const Gap(32),
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
