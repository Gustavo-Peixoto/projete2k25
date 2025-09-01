import mysql.connector
import hashlib

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "gu010104",
    database =  "projete2k25"
)

cursor = db.cursor()
def add(nome, email, senha):
    hash = hashlib.sha256(senha.encode())
    senhahash = hash.hexdigest()

    cursor.execute("SELECT * FROM login WHERE email = %s", (email,))

    result = cursor.fetchone()

    if(result):
        return "Email ja cadastrado."
    else:
        cursor.execute("INSERT INTO login (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senhahash))
        db.commit()
        print(cursor.rowcount, "Feito")

    cursor.close()
    db.close()

    return "Cadastrado com sucesso."
        





