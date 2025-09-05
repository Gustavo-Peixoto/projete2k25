import os
import mysql.connector
import base64

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Crime#18",
    database =  "projete2k25"
)
cursor = db.cursor()

def salvarPdf(usuario_id, nomeUser, pdfByte):
    caminho = ""
    nome = ""
    cont = 1
    while True:
        nome = f"pdf{cont}.pdf"
        caminho = os.path.join("uploads", nome)
        if not os.path.exists(caminho):
            break
        cont += 1

    cursor.execute("SELECT * FROM clientes WHERE usuario_id = %s AND caminho = %s", (usuario_id, caminho,))
    result = cursor.fetchone()

    if(result):
        return {
            "codigo" : 100,
            "mensagem" : "nome do arquivo ja existe pro usuario",
            "caminho" : None
        }
    
    try:
        pdf = base64.b64decode(pdfByte)
        with open(caminho, "wb") as f:
            f.write(pdf)
        cursor.execute("INSERT INTO clientes (usuario_id, nome_arquivo, nome_servidor, caminho, tipo, data) VALUES (%s,%s,%s,%s,%s,NOW())", (usuario_id,nomeUser,nome,caminho,"pdf",))
        db.commit()
        return {
            "codigo" : 200,
            "mensagem": "salvo com sucesso",
            "caminho" : caminho
        }
    except Exception as e:
        return {
            "codigo" : 400,
            "mensagem" : f"erro a salvar:{str(e)}",
            "caminho" : None
        }
    finally:
        cursor.close()
        db.close()

