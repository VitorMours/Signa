import 'package:flutter/material.dart';
import 'package:mobile/core/components/form_input.dart';
import 'package:gap/gap.dart';
import 'package:go_router/go_router.dart';

class SigninPage extends StatefulWidget {
  const SigninPage({super.key});

  @override
  SigninPageState createState() {
    return SigninPageState();
  }
}

class SigninPageState extends State<SigninPage> {
  final _loginFormKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Padding(
                padding: EdgeInsets.all(24),
                child: Form(
                  key: _loginFormKey,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text("Signa"),
                      Row(
                        children: [
                          Expanded(
                            child: FormInput(
                              validator: (String? value) {
                                if (value!.isEmpty || value.trim() == "") {
                                  return "Please input text";
                                }
                              },
                              labelText: 'Nome',
                              hintText: 'John',
                            ),
                          ),
                          SizedBox(width: 16),
                          Expanded(
                            child: FormInput(
                              validator: (String? value) {
                                if (value!.isEmpty || value.trim() == "") {
                                  return "Please input text";
                                }
                              },
                              labelText: 'Sobrenome',
                              hintText: 'Doe',
                            ),
                          ),
                        ],
                      ),

                      Gap(12),
                      FormInput(
                        validator: (String? value) {
                          if (value!.isEmpty || value.trim() == "") {
                            return "Please input text";
                          }
                          return null;
                        },
                        labelText: 'Email',
                        hintText: 'Enter your email',
                      ),
                      Gap(12),

                      FormInput(
                        validator: (String? value) {
                          if (value!.isEmpty || value.trim() == "") {
                            return "Please input text";
                          }
                          return null;
                        },
                        labelText: 'Senha',
                        hintText: 'Digite sua senha',
                      ),
                      Gap(12),
                      FormInput(
                        validator: (String? value) {
                          if (value!.isEmpty || value.trim() == "") {
                            return "Please input text";
                          }
                          return null;
                        },
                        labelText: 'Repita sua Senha',
                        hintText: 'Digite a senha de novo',
                      ),
                      Align(
                        alignment: Alignment.centerRight,
                        child: TextButton(
                          onPressed: () => context.go('/login'),
                          child: Text("Ja possui conta?"),
                        ),
                      ),
                      Gap(42),
                      Center(
                        child: ElevatedButton(
                          onPressed: () {
                            if (_loginFormKey.currentState!.validate()) {
                              // Perform login action
                            }
                          },
                          child: Text("Criar Conta"),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
