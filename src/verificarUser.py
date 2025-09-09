import mysql.connector
import hashlib

def verificar(senha, email, cursor):
    hash = hashlib.sha256(senha.encode())
    senhahash = hash.hexdigest()
    cursor.execute("SELECT 1 FROM login WHERE email = %s AND senha = %s", (email,senhahash,))
    result = cursor.fetchone()
    if result is not None:
        return {
            'codigo' : 200,
            'mensagem' : 'login feito.'
        }
    else:
        return {
            'codigo' : 400,
            'mensagem' : 'Senha ou email incorreto.'
        }