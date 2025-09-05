import os
import base64

nome = "teste.pdf"

with open(nome, "rb") as f:
    pdf = f.read()

pdf64 = base64.b64encode(pdf)

pdf = base64.b64decode(pdf64)
caminho = os.path.join("uploads", nome)
if(os.path.exists(caminho)):
    print("Existe")
else:
    with open(caminho, "wb") as r:
        r.write(pdf)

