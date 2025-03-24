import 'package:flutter/material.dart';
import '../services/api_service.dart';
import 'home_screen.dart';
import '../theme.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();
  final api = ApiService();

  Future<void> _handleLogin() async {
    try {
      final response = await api.loginUser(
        emailController.text,
        passwordController.text,
      );
      final userId = response["user_id"];
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (_) => HomeScreen(userId: userId)),
      );
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("Login fehlgeschlagen")),
      );
    }
  }

  void _showRegisterDialog() {
    String name = '';
    String email = '';
    String password = '';

    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: backgroundGreen,
        title: Text("Registrieren", style: TextStyle(color: Colors.white)),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            TextField(
              style: TextStyle(color: Colors.white),
              decoration: InputDecoration(labelText: "Name", labelStyle: TextStyle(color: lightGreen)),
              onChanged: (value) => name = value,
            ),
            TextField(
              style: TextStyle(color: Colors.white),
              decoration: InputDecoration(labelText: "E-Mail", labelStyle: TextStyle(color: lightGreen)),
              onChanged: (value) => email = value,
            ),
            TextField(
              obscureText: true,
              style: TextStyle(color: Colors.white),
              decoration: InputDecoration(labelText: "Passwort", labelStyle: TextStyle(color: lightGreen)),
              onChanged: (value) => password = value,
            ),
          ],
        ),
        actions: [
          TextButton(
            child: Text("Abbrechen", style: TextStyle(color: Colors.grey)),
            onPressed: () => Navigator.pop(context),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(backgroundColor: accentGreen),
            child: Text("Registrieren"),
            onPressed: () async {
              try {
                await api.createUser(name, email, password);
                Navigator.pop(context);
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text("Erfolgreich registriert")),
                );
              } catch (e) {
                Navigator.pop(context);
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text("Fehler bei der Registrierung")),
                );
              }
            },
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: darkGreen,
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(32),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("SOLD", style: TextStyle(color: lightGreen, fontSize: 40, fontWeight: FontWeight.bold)),
              SizedBox(height: 40),
              TextField(
                controller: emailController,
                style: TextStyle(color: Colors.white),
                decoration: InputDecoration(
                  labelText: "E-Mail",
                  labelStyle: TextStyle(color: lightGreen),
                  enabledBorder: UnderlineInputBorder(borderSide: BorderSide(color: lightGreen)),
                ),
              ),
              TextField(
                controller: passwordController,
                obscureText: true,
                style: TextStyle(color: Colors.white),
                decoration: InputDecoration(
                  labelText: "Passwort",
                  labelStyle: TextStyle(color: lightGreen),
                  enabledBorder: UnderlineInputBorder(borderSide: BorderSide(color: lightGreen)),
                ),
              ),
              SizedBox(height: 30),
              ElevatedButton(
                onPressed: _handleLogin,
                style: ElevatedButton.styleFrom(
                  backgroundColor: accentGreen,
                  minimumSize: Size(double.infinity, 50),
                ),
                child: Text("Login"),
              ),
              TextButton(
                onPressed: _showRegisterDialog,
                child: Text("Jetzt registrieren", style: TextStyle(color: lightGreen)),
              )
            ],
          ),
        ),
      ),
    );
  }
}
