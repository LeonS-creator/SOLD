import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'screens/login_screen.dart';
import 'screens/home_screen.dart';
import 'theme.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // Async-Initialisierung, um den ersten Screen zu bestimmen
  Future<Widget> _getInitialScreen() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final userId = prefs.getInt('userId');
      if (userId != null) {
        return HomeScreen(userId: userId); // Falls User existiert, gehe zum HomeScreen
      } else {
        return LoginScreen(); // Andernfalls zum LoginScreen
      }
    } catch (e) {
      return ErrorScreen(errorMessage: 'Fehler beim Laden des Nutzers: $e'); // Fehlerbehandlung
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SOLD App',
      theme: ThemeData(
        primarySwatch: Colors.green,
        scaffoldBackgroundColor: backgroundGreen,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      debugShowCheckedModeBanner: false,
      home: FutureBuilder<Widget>(
        future: _getInitialScreen(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Scaffold(
              body: Center(child: CircularProgressIndicator()), // SplashScreen/Loading
            );
          } else if (snapshot.hasError) {
            return Scaffold(
              body: Center(child: Text("Fehler: ${snapshot.error}", style: TextStyle(color: Colors.white))),
            );
          } else if (snapshot.hasData) {
            return snapshot.data!;
          } else {
            return ErrorScreen(errorMessage: 'Unbekannter Fehler');
          }
        },
      ),
    );
  }
}

// Error Screen (kann verwendet werden, wenn etwas nicht geladen wird)
class ErrorScreen extends StatelessWidget {
  final String errorMessage;
  const ErrorScreen({Key? key, required this.errorMessage}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.red,
      body: Center(
        child: Text(
          errorMessage,
          style: TextStyle(color: Colors.white, fontSize: 18),
        ),
      ),
    );
  }
}
