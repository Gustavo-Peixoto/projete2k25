import hashlib

def verificar(senha, email, cursor):
    hash = hashlib.sha256(senha.encode())
    senhahash = hash.hexdigest()
    cursor.execute("SELECT id FROM login WHERE email = %s AND senha = %s", (email,senhahash,))
    usuario = cursor.fetchone()
    if usuario:
        usuarioId = usuario[0]
        return {
            'codigo' : 200,
            'mensagem' : 'login feito.',
            'usuarioId' : usuarioId
        }
    else:
        return {
            'codigo' : 400,
            'mensagem' : 'Senha ou email incorreto.',
            'usuarioId' : None
        }