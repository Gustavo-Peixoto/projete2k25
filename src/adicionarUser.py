import hashlib

def add(nome, email, senha, db, cursor):
    hash = hashlib.sha256(senha.encode())
    senhahash = hash.hexdigest()

    cursor.execute("SELECT 1 FROM login WHERE email = %s", (email,))

    result = cursor.fetchone()

    if result:
        return {
            'codigo' : 400,
            'mensagem' : 'email ja existente'
        }
    else:
        cursor.execute("INSERT INTO login (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senhahash))
        db.commit()
        print(cursor.rowcount, "Feito")
        return{
            'codigo' : 200,
            'mensagem' : 'cadastrado com sucesso'
        }
        





