import 'package:flutter/material.dart';
import 'package:qr_flutter/qr_flutter.dart';
import '../theme.dart';

class QRCodeScreen extends StatelessWidget {
  final int userId;
  const QRCodeScreen({Key? key, required this.userId}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final String qrData = "SOLD-USER-$userId"; // Später dynamisch von DB

    return Container(
      decoration: BoxDecoration(
        color: backgroundGreen,
        borderRadius: BorderRadius.vertical(top: Radius.circular(25)),
      ),
      padding: EdgeInsets.all(32),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Text("Dein QR-Code", style: TextStyle(color: Colors.white, fontSize: 20)),
          SizedBox(height: 20),
          QrImageView(
            data: qrData,
            version: QrVersions.auto,
            size: 200.0,
            backgroundColor: Colors.white,
          ),
          SizedBox(height: 20),
          Text("Zeige diesen Code an der Kasse vor.", style: TextStyle(color: lightGreen)),
        ],
      ),
    );
  }
}