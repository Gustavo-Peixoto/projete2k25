import requests

dados = {
    'usuario_id': 10,
    'nome': 'Gustavo',
    'nome_animal': 'Rex',
    'telefone': '11999999999',
    'email': 'gustavo@email.com',
    'endereco': 'Rua Exemplo, 123'
}

resposta = requests.post("http://localhost:5000/clientes",json=dados)

print(resposta.status_code)
print(resposta.json())