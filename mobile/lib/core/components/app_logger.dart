import "package:logger/logger.dart";




class AppLogger {
  // 1. Initialize the Logger with custom formatting
  static final Logger _logger = Logger(
    printer: PrettyPrinter(
      methodCount: 2,         // Number of method calls to be displayed
      errorMethodCount: 8,    // Number of method calls if stacktrace is provided
      lineLength: 120,        // Width of the output
      colors: true,           // Colorful log messages
      printEmojis: true,      // Print an emoji for each log type
      printTime: true,        // Should each log print contain a timestamp?
    ),
    // 2. Automatically filter logs so they don't print in Production
    filter: DevelopmentFilter(),
  );

  // 3. Expose clean, static methods for the app to use
  static void d(String message) => _logger.d(message); // Debug
  static void i(String message) => _logger.i(message); // Info
  static void w(String message) => _logger.w(message); // Warning
  static void e(String message, [dynamic error, StackTrace? stackTrace]) {
    _logger.e(message, error: error, stackTrace: stackTrace); // Error
  }
}
