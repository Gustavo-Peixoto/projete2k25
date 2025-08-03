import 'dart:convert'; // base64 decode
import 'dart:io'; // File
import 'dart:typed_data'; // Uint8List

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const MaterialApp(home: EnviarImagem()));
}

class EnviarImagem extends StatefulWidget {
  const EnviarImagem({super.key});

  @override
  State<EnviarImagem> createState() => _EnviarImagemState();
}

class _EnviarImagemState extends State<EnviarImagem> {
  File? _imagemOriginal;
  Uint8List? _imagemProcessadaBytes;
  bool _enviando = false;

  Future<void> selecionarEEnviarImagem() async {
    final picker = ImagePicker();
    final imagemSelecionada = await picker.pickImage(
      source: ImageSource.gallery,
    );

    if (imagemSelecionada == null) return;

    setState(() {
      _imagemOriginal = File(imagemSelecionada.path);
      _imagemProcessadaBytes = null;
      _enviando = true;
    });

    final uri = Uri.parse(
      'http://10.0.2.2:5000/image_proces',
    ); // IP do host para emulador Android

    var request = http.MultipartRequest('POST', uri);
    request.files.add(
      await http.MultipartFile.fromPath('img', _imagemOriginal!.path),
    );

    try {
      var resposta = await request.send();

      if (resposta.statusCode == 200) {
        var respostaBody = await resposta.stream.bytesToString();
        var jsonResposta = json.decode(respostaBody);

        String imagemBase64 = jsonResposta['imagem'];

        setState(() {
          _imagemProcessadaBytes = base64Decode(imagemBase64);
        });
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Erro ao enviar imagem: ${resposta.statusCode}'),
          ),
        );
      }
    } catch (e) {
      ScaffoldMessenger.of(
        context,
      ).showSnackBar(SnackBar(content: Text('Erro de conexão: $e')));
    } finally {
      setState(() {
        _enviando = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Enviar Imagem para Flask")),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              _imagemOriginal != null
                  ? Column(
                      children: [
                        const Text('Imagem Original:'),
                        const SizedBox(height: 8),
                        Image.file(_imagemOriginal!, height: 200),
                        const SizedBox(height: 20),
                      ],
                    )
                  : const Text("Nenhuma imagem selecionada."),

              _imagemProcessadaBytes != null
                  ? Column(
                      children: [
                        const Text('Imagem Processada:'),
                        const SizedBox(height: 8),
                        Image.memory(_imagemProcessadaBytes!, height: 200),
                        const SizedBox(height: 20),
                      ],
                    )
                  : Container(),

              ElevatedButton(
                onPressed: _enviando ? null : selecionarEEnviarImagem,
                child: _enviando
                    ? const CircularProgressIndicator(color: Colors.white)
                    : const Text("Selecionar e Enviar Imagem"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
