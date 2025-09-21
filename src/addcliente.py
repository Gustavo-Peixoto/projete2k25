
def criar(usuario_id,nome,nome_animal,telefone,email,endereco,db,cursor):
    cursor.execute("SELECT 1 FROM clientes WHERE nome = %s AND nome_animal = %s AND telefone = %s",(nome,nome_animal,telefone,))
    result = cursor.fetchone()
    if result is not None:
        return{
            'codigo' : 500,
            'mensagem' : 'Cliente ja existe'
        }
    else:
        cursor.execute("INSERT INTO clientes (usuario_id,nome,nome_animal,telefone,email,endereco) VALUES (%s,%s,%s,%s,%s,%s)", (usuario_id, nome, nome_animal, telefone, email, endereco))
        db.commit()
        return{
            'codigo' : 200,
            'mensagem' : 'Cliente criado com sucesso.'
        }
        
