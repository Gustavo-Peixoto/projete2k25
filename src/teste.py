import os
import base64

nome = "teste.pdf"

with open(nome, "rb") as f:
    pdf = f.read()

pdf64 = base64.b64encode(pdf)

pdf = base64.b64decode(pdf64)


caminho = os.path.join("uploads", nome)

with open(caminho, "wb") as r:
    r.write(pdf)
