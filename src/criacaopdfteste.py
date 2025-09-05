import requests
import base64

with open("teste.pdf","rb") as f:
    pdf = base64.b64encode(f.read()).decode("utf-8")

dados = {
    "usuario_id" : 15,
    "nome_arquivo" : "teste.pdf",
    "relatorio" : pdf
}

url = "http://localhost:5000/relatorios"

request = requests.post(url, json=dados)

print(request.status_code)
print(request.json())