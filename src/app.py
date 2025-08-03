import cv2
import numpy as np
import base64
from flask import Flask, request, jsonify
import processamento
# seu processamento continua igual...

def imagem_para_base64(imagem_np):
    _, buffer = cv2.imencode('.jpg', imagem_np)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')
    return jpg_as_text

server = Flask(__name__)

@server.route('/image_proces', methods=['POST'])
def receber_imagem():
    if 'img' not in request.files:
        return jsonify({'erro': 'Nenhuma imagem recebida'}), 400

    file = request.files['img']
    imagem_bytes = file.read()

    resultado = processamento.processar_imagem(imagem_bytes)

    imagem_b64 = imagem_para_base64(resultado)

    return jsonify({"mensagem": "sucesso", "imagem": imagem_b64}), 200

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000, debug=True)
