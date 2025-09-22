import processamento
import adicionarUser
import hashlib
import addcliente
import cv2
import numpy as np
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
import json

os.makedirs("uploads", exist_ok=True)

db = mysql.connector.connect(
    host = "localhost",
    user = "projete",
    password = "Climb#18",
    database =  "projete2k25"
)

cursor = db.cursor(dictionary=True)

def imagem_para_base64(imagem_np):
    _, buffer = cv2.imencode('.jpg', imagem_np)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')
    return jpg_as_text

server = Flask(__name__)
CORS(server)

@server.route('/imageProces', methods=['POST'])
def processarImagem():
    if 'img' not in request.files:
        return jsonify({'erro': 'Nenhuma imagem recebida'}), 400

    file = request.files['img']
    imagem_bytes = file.read()

    resultado = processamento.processar_imagem(imagem_bytes)
    imagem_b64 = imagem_para_base64(resultado)

    return jsonify({"mensagem": "sucesso", "imagem": imagem_b64}), 200

@server.route("/verifyclientes", methods=['POST'])
def mostrarClientes():
    try:
        dados = request.json
        user = dados.get("usuarioId")
        if user is None:
            return jsonify({'mensagem' : 'É nescessario o id do usuario', 'clientes' : None}), 400
        
        cursor.execute("SELECT * FROM clientes WHERE usuario_id = %s",(user,))
        lista = cursor.fetchall()

        if lista:
            return jsonify({'mensagem' : "Sucesso.",'clientes' : lista}), 200
        else:
            return jsonify({'mensagem' : "Nenhum cliente",'clientes' : []}), 200
        
    except Exception as a:
        return jsonify({'mensagem' : f"Erro: {a}", 'clientes' : None}), 400


@server.route("/clientes", methods=['POST'])
def criarCliente():
    try:
        dados = request.json
        result = addcliente.criar(
            dados['usuarioid'],
            dados['nome'],
            dados['nomeAnimal'],
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
def verficarUser():
    try:
        dados = request.json
        email = dados.get("email")
        senha = dados.get("senha")

        if not email or not senha:
            return jsonify({'codigo': 400, 'mensagem': 'Email e senha são obrigatórios.', 'usuarioId': None}), 400

        hash = hashlib.sha256(senha.encode())
        senhahash = hash.hexdigest()

        cursor.execute("SELECT id FROM login WHERE email = %s AND senha = %s", (email,senhahash,))
        usuario = cursor.fetchone()

        if usuario:
            return jsonify({
                'mensagem' : 'login feito.',
                'usuarioId' : usuario
            }), 200
        
        else:
            return jsonify({
                'mensagem' : 'Senha ou email incorreto.',
                'usuarioId' : None
            }), 400
        
    except Exception as e:
        print("Erro em /verifyuser:", e) 
        return jsonify({'codigo': 500, 'mensagem': f'Erro interno: {e}', 'usuarioId': None}), 500

@server.route('/adduser', methods=['POST'])
def adicionar_user():
    dados = request.json
    resposta = adicionarUser.add(dados["nome"], dados["email"], dados["senha"], db, cursor)
    return jsonify(resposta), resposta['codigo']

@server.route('/addexame', methods=['POST'])
def adicionarExame():
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
    
@server.route('/verifyexame', methods=['POST'])
def listarExames():
    try:
        dados = request.json
        cliente_id = dados.get("clienteId")

        if cliente_id is None:
            return jsonify({'Mensagem' : "É nescessario o id do cliente", 'exames' : None}), 400
        
        cursor.execute("SELECT * FROM exames WHERE cliente_id = %s", (cliente_id,))
        lista = cursor.fetchall()
        
        if lista:
            return jsonify({'mensagem' : 'Sucesso', 'exames' : lista}), 200
        else:
            return jsonify({'mensagem' : "Nao existe exames.", 'exames' : []}), 200
        
    except Exception as a:
        return jsonify({'mensagem' : f"Erro: {a}", 'exames' : None}), 400
        

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=5000, debug=True)
