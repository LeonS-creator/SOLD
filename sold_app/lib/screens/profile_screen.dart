import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'login_screen.dart';
import '../theme.dart';

class ProfileScreen extends StatelessWidget {
  final int userId;
  const ProfileScreen({Key? key, required this.userId}) : super(key: key);

  Future<void> _logout(BuildContext context) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('userId');
    Navigator.pushAndRemoveUntil(
      context,
      MaterialPageRoute(builder: (context) => LoginScreen()),
          (route) => false,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text("Profil", style: TextStyle(color: lightGreen, fontSize: 28, fontWeight: FontWeight.bold)),
          SizedBox(height: 24),
          Text("Nutzer-ID: $userId", style: TextStyle(color: Colors.white)),
          SizedBox(height: 12),
          Text("Gesammelte Punkte: wird geladen...", style: TextStyle(color: lightGreen)),
          SizedBox(height: 30),
          ElevatedButton(
            onPressed: () => _logout(context),
            style: ElevatedButton.styleFrom(backgroundColor: accentGreen),
            child: Text("Logout"),
          )
        ],
      ),
    );
  }
}
