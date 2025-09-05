import requests

dados = {
    "nome": "Gustavo",
    "email": "teste2@email.com",
    "senha": "78910"
}

url = "http://localhost:5000/usuarios"

resposta = requests.post(url, json=dados)

print(resposta.status_code)
print(resposta.json())