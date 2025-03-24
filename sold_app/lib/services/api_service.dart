import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl =  "http://10.0.2.2:8001"; //"http://127.0.0.1:8000"; // API-URL

  Future<Map<String, dynamic>> createUser(String name, String email, String password) async {
    final url = Uri.parse('$baseUrl/users/');
    final response = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "name": name,
        "email": email,
        "password": password,
      }),
    );

    if (response.statusCode == 200 || response.statusCode == 201) {
      return jsonDecode(response.body);
    } else {
      throw Exception("Fehler: ${response.statusCode} - ${response.body}");
    }
  }
  Future<Map<String, dynamic>> loginUser(String email, String password) async {
    final url = Uri.parse('$baseUrl/login/');
    final response = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "email": email,
        "password": password,
      }),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception("Login fehlgeschlagen: ${response.statusCode} - ${response.body}");
    }
  }

}
