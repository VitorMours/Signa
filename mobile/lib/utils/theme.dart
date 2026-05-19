import "package:flutter/material.dart";
import "package:google_fonts/google_fonts.dart";

class AppTheme {
  static ThemeData dark = ThemeData(
    textSelectionTheme: TextSelectionThemeData(
      selectionColor: AppColors.tertiary.withValues(alpha: 0.3),
      cursorColor: AppColors.tertiary,
    ),
    inputDecorationTheme: AppInputTheme.appInputTheme,
    elevatedButtonTheme: ElevatedButtonTheme.elevatedButton,
    textTheme: GoogleFonts.lexendTextTheme(),
    useMaterial3: true,
    brightness: Brightness.light,
    colorScheme: const ColorScheme.light(
      primary: AppColors.primary,
      secondary: AppColors.secondary,
      tertiary: AppColors.tertiary,
      surface: AppColors.surface,
    ),

    scaffoldBackgroundColor: AppColors.background,
  );
}

class AppColors {
  static const primary = Color.fromARGB(255, 0, 184, 216);
  static const secondary = Color.fromARGB(255, 43, 122, 225);
  static const tertiary = Color(0xFF502BE0);
  static const background = Color.fromARGB(255, 239, 239, 239);
  static const surface = Color.fromARGB(255, 221, 226, 228);
  static const text = Colors.black;
  static const hintText = Color.fromARGB(255, 145, 145, 145);
  static const whiteText = Colors.white;
}

class ElevatedButtonTheme {
  static final elevatedButton = ElevatedButtonThemeData(
    style: ElevatedButton.styleFrom(
      backgroundColor: AppColors.tertiary,
      foregroundColor: AppColors.whiteText,
      fixedSize: const Size(150, 50),
      textStyle: TextStyle(fontWeight: FontWeight.bold),
      padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 14),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(25)),
    ),
  );
}

class AppInputTheme {
  static InputDecorationTheme appInputTheme = InputDecorationTheme(
    filled: true,
    fillColor: const Color(0xFFFFFFFF),
    hoverColor: const Color(0xFFFFFFFF),
    hintStyle: TextStyle(color: AppColors.hintText),
    prefixStyle: TextStyle(color: AppColors.hintText),

    border: OutlineInputBorder(
      borderRadius: BorderRadius.circular(12),
      borderSide: const BorderSide(color: Color(0xFF9F9F9F), width: 2),
    ),
    enabledBorder: OutlineInputBorder(
      borderRadius: BorderRadius.circular(12),
      borderSide: const BorderSide(
        color: Color.fromARGB(255, 43, 43, 43),
        width: 2,
      ),
    ),

    focusedBorder: OutlineInputBorder(
      borderRadius: BorderRadius.circular(12),
      borderSide: const BorderSide(color: AppColors.tertiary, width: 2),
    ),
  );
}
