import 'package:flutter/material.dart';
import '../theme.dart';

class StoreListScreen extends StatelessWidget {
  final int userId;
  const StoreListScreen({Key? key, required this.userId}) : super(key: key);

  final List<Map<String, String>> dummyStores = const [
    {"name": "Bäckerei Kruste", "category": "Backwaren"},
    {"name": "Grüne Apotheke", "category": "Gesundheit"},
    {"name": "Bio Markt", "category": "Lebensmittel"},
  ];

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      padding: EdgeInsets.all(16),
      itemCount: dummyStores.length,
      itemBuilder: (context, index) {
        final store = dummyStores[index];
        return Card(
          color: darkGreen,
          margin: EdgeInsets.symmetric(vertical: 8),
          child: ListTile(
            title: Text(store['name']!, style: TextStyle(color: Colors.white)),
            subtitle: Text(store['category']!, style: TextStyle(color: lightGreen)),
            trailing: Icon(Icons.arrow_forward_ios, color: lightGreen, size: 16),
            onTap: () {
              // TODO: Detailansicht mit Aktionen
            },
          ),
        );
      },
    );
  }
}