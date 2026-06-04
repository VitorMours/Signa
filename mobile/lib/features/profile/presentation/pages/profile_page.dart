import "package:flutter/material.dart";
import "package:mobile/core/components/form_input.dart";
import "package:gap/gap.dart";

class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {
    final _formKey = GlobalKey<FormState>();

    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 24.0),
        child: Column(
          children: <Widget>[
            Text("Informacoes Pessoais"),
            Form(
              key: _formKey,
              child: Column(
                children: <Widget>[
                  Row(
                    children: <Widget>[
                      Expanded(
                        child: FormInput(
                          labelText: 'Primeiro Nome',
                          hintText: 'Johgn',
                          validator: (String? p1) {},
                        ),
                      ),
                      Gap(16),
                      Expanded(
                        child: FormInput(
                          labelText: 'Sobrenome',
                          hintText: 'Doee',
                          validator: (String? p1) {},
                        ),
                      ),
                    ],
                  ),
                  FormInput(
                    labelText: 'Email',
                    hintText: 'Johgn',
                    validator: (String? p1) {},
                  ),
                  FormInput(
                    labelText: 'Especializacao',
                    hintText: 'Johgn',
                    validator: (String? p1) {},
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
