import requests

dados = {
    "nome": "Gustavo",
    "email": "teste@email.com",
    "senha": "123456"
}

url = "http://localhost:5000/usuarios"

resposta = requests.post(url, json=dados)

print(resposta.status_code)
print(resposta.json())