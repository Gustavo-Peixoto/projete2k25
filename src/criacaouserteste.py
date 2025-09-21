import requests

dados = {
    'nome' : "gustavo",
    'email' : "tes",
    'senha' : "12333"
}

resposta = requests.post("http://172.20.10.2:5000/adduser",json=dados)


print(resposta.status_code)
print(resposta.json())