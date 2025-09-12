import requests

dados = {
    "cliente_id": 1,
    "alimentos": {
        "carne_bovina": "positivo",
        "carne_frango": "negativo",
        "carne_porco": "negativo",
        "ovo_galinha": "positivo",
        "leite_vaca": "negativo",
        "soja": "negativo",
        "trigo": "positivo",
        "milho": "negativo",
        "peixe": "negativo",
        "camarão": "positivo",
        "ervilha": "negativo",
        "cenoura": "positivo",
        "batata": "negativo",
        "abobora": "negativo",
        "maçã": "positivo",
        "banana": "negativo"
  },
  "peso": 72,
  "sexo": "M"
}

resposta = requests.post("http://localhost:5000/addexame", json=dados)
print(resposta.status_code)
print(resposta.json())