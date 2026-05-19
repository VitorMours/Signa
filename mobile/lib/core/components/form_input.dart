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
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Padding(
          padding: const EdgeInsets.fromLTRB(8.0, 0, 0, 8),
          child: Text(widget.labelText, style: TextStyle(fontWeight: FontWeight.bold),textAlign: TextAlign.left),
        ),
        TextFormField(
          decoration: InputDecoration(
            hintText: widget.hintText,
          ),
          validator: widget.validator,
        ),
      ],
    );
  }
}
