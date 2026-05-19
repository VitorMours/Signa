import 'package:flutter/material.dart';
import 'package:mobile/core/components/form_input.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  LoginPageState createState() {
    return LoginPageState();
  }
}

class LoginPageState extends State<LoginPage> {
  final _loginFormKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
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
                  Text("Email", textAlign: TextAlign.left),
                  FormInput(
                    validator: (String? value) {
                      if (value!.isEmpty || value.trim() == "") {
                        return "Please input text";
                      }
                      return null;
                    },
                    labelText: '',
                    hintText: 'Enter your email',
                  ),
                  Text("Senha", textAlign: TextAlign.left),
                  FormInput(
                    validator: (String? value) {
                      if (value!.isEmpty || value.trim() == "") {
                        return "Please input text";
                      }
                    },
                    labelText: '',
                    hintText: 'Enter your password',
                  ),
                  ElevatedButton(
                    onPressed: () {
                      if (_loginFormKey.currentState!.validate()) {
                        // Perform login action
                      }
                    },
                    child: Text("Login"),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
