import requests

dados = {
    'clienteId' : 1
}

resposta = requests.post("http://localhost:5000/verifyexame",json=dados)


print(resposta.status_code)
print(resposta.json())
