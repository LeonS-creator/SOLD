/*
import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  final int userId;

  const HomeScreen({Key? key, required this.userId}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Willkommen!'),
      ),
      body: Center(
        child: Text('Eingeloggt als User-ID: $userId'),
      ),
    );
  }
}
*/

import 'package:flutter/material.dart';
import 'qr_code_screen.dart';
import 'profile_screen.dart';
import 'store_list_screen.dart'; // dein Geschäftelisting
import '../theme.dart';

class HomeScreen extends StatefulWidget {
  final int userId;
  const HomeScreen({Key? key, required this.userId}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 0;

  final List<Widget> _pages = [];

  @override
  void initState() {
    super.initState();
    _pages.addAll([
      StoreListScreen(userId: widget.userId),
      Container(), // Platzhalter für QR
      ProfileScreen(userId: widget.userId),
    ]);
  }

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  void _showQRModal() {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (_) => QRCodeScreen(userId: widget.userId),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: backgroundGreen,
      body: IndexedStack(
        index: _selectedIndex == 1 ? 0 : _selectedIndex,
        children: _pages,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _showQRModal,
        backgroundColor: accentGreen,
        child: Icon(Icons.qr_code, color: Colors.white),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
      bottomNavigationBar: BottomAppBar(
        color: darkGreen,
        shape: CircularNotchedRectangle(),
        notchMargin: 8,
        child: SizedBox(
          height: 60,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              IconButton(
                icon: Icon(Icons.store, color: _selectedIndex == 0 ? lightGreen : Colors.white),
                onPressed: () => _onItemTapped(0),
              ),
              SizedBox(width: 40), // Platz für QR
              IconButton(
                icon: Icon(Icons.person, color: _selectedIndex == 2 ? lightGreen : Colors.white),
                onPressed: () => _onItemTapped(2),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
