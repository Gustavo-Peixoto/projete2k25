import processamento
import adicionarUser
import cv2
import numpy as np
import base64
from flask import Flask, request, jsonify
import mysql.connector
import os

os.makedirs("uploads", exist_ok=True)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "gu010104",
    database =  "projete2k25"
)

cursor = db.cursor()

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

@server.route("/relatorios", mehtods=['POST'])
def criarRelatorio():
    dados = request.json
    nome = dados["nome_arquivo"]
    caminho = os.path.join("./upload", nome)
    pdf_bytes = base64.b64decode(dados["relatorio"])

    with open(caminho, 'wb') as f:
        f.write(pdf_bytes)
    


@server.route('/usuarios', methods=['POST'])
def adicionar_user():
    dados = request.get_json()
    resposta = adicionarUser.add(dados["nome"], dados["email"], dados["senha"])
    return jsonify({"mensagem": "sucesso", "estado": resposta}), 200

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000, debug=True)
