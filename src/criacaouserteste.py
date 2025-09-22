import requests

dados = {
    'nome' : "gustavo",
    'email' : "testada",
    'senha' : "123"
}

resposta = requests.post("http://localhost:5000/adduser",json=dados)


print(resposta.status_code)
print(resposta.json())