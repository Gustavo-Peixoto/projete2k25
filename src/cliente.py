import requests

caminho_imagem = 'imagem.jpg'  

url = 'http://localhost:5000/image_proces'  

with open(caminho_imagem, 'rb') as img:
    arquivos = {'img': img}
    resposta = requests.post(url, files=arquivos)
print('Status:', resposta.status_code)

print(resposta.json()['mensagem'])
