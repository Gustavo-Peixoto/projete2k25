import processamento
import adicionarUser
import verificarUser
import addcliente
import cv2
import numpy as np
import base64
from flask import Flask, request, jsonify
import mysql.connector
import os
import json

os.makedirs("uploads", exist_ok=True)

db = mysql.connector.connect(
    host = "localhost",
    user = "gustv",
    password = "Climb#18",
    database =  "projete2k25"
)

cursor = db.cursor(dictionary=True)

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

@server.route("/verifyrelatorios", methods=['POST'])
def mostrarClientes():
    try:
        dados = request.json
        user = dados["usuario_id"]
        cursor.execute("SELECT * FROM clientes WHERE usuario_id = %s",(user,))
        lista = cursor.fetchall()
        return jsonify({'mensagem' : "Sucesso.",'clientes' : lista}), 200
    except Exception as a:
        return jsonify({'mensagem' : f"Erro: {a}", 'clientes' : None}), 400


@server.route("/clientes", methods=['POST'])
def criarRelatorio():
    try:
        dados = request.json
        result = addcliente.criar(
            dados['usuario_id'],
            dados['nome'],
            dados['nome_animal'],
            dados['telefone'],
            dados['email'],
            dados['endereco'],
            db,
            cursor
            )
        return jsonify(result), result['codigo']
    except Exception as f:
        return jsonify({'mensagem' : f"erro: {f}"}), 400

@server.route('/verifyuser', methods=['POST'])
def verficar_user():
    dados = request.json
    email = dados["email"]
    senha = dados["senha"]
    resultado = verificarUser.verificar(senha, email, db, cursor)
    return jsonify(resultado), resultado['codigo']

@server.route('/adduser', methods=['POST'])
def adicionar_user():
    dados = request.get_json()
    resposta = adicionarUser.add(dados["nome"], dados["email"], dados["senha"], db, cursor)
    return jsonify(resposta), resposta['codigo']

@server.route('/addexame', methods=['POST'])
def adicionar_exame():
    try:
        dados = request.json
        clienteId = dados["cliente_id"]
        alimentos = json.dumps(dados["alimentos"])
        peso = dados["peso"]
        sexo = dados["sexo"]
        cursor.execute("INSERT INTO exames (alimentos,peso,sexo,cliente_id) VALUES (%s,%s,%s,%s)",(alimentos,peso,sexo,clienteId))
        db.commit()
        return jsonify({'mensagem' : 'Criado com sucesso.'}), 200
    except Exception as a:
        return jsonify({'mensagem' : f'erro:{a}'}), 400

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000, debug=True)
