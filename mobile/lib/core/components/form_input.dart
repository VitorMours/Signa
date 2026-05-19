import 'package:flutter/material.dart';

class FormInput extends StatefulWidget {
  const FormInput({
    super.key,
    required this.validator,
    required this.labelText,
    required this.hintText,
  });

  final String? Function(String?) validator;
  final String labelText;
  final String hintText;

  @override
  State<FormInput> createState() => _FormInputState();
}

class _FormInputState extends State<FormInput> {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        TextFormField(
          decoration: InputDecoration(
            labelText: widget.labelText,
            hintText: widget.hintText,
          ),
          validator: widget.validator,
        ),
      ],
    );
  }
}
