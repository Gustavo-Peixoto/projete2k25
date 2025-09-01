import os
import base64

os.makedirs("./upload", exist_ok=True)

nome = "teste.pdf"
caminho = os.path.join("./upload", nome)
valid_base64 = base64.b64encode(b"meu conteudo").decode('utf-8')
pdf_bytes = base64.b64decode(valid_base64)
with open(caminho, 'wb') as f:
    f.write(pdf_bytes)

print(caminho)