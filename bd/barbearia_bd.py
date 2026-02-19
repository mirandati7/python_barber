from bd.conexao import conecta_db

# DML = Linguagem de manipulação de Dados
#CRUD => Create, Read, Update , Delete
#        INSERT, SELECT , UPDATE, DELETE 

# DDL = Linguagem de Criação de tabelas
#  Create table 
#  DROP table
#  Alter table 

def listar_barbearia_bd(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
              select id,nome,telefone,endereco,forma_pagamento
              from barbearia order by id asc""")
    registros = cursor.fetchall()
    return registros


def inserir_barbearia_bd(conexao, nome,telefone,endereco,forma_pagamento):
    cursor = conexao.cursor()
    sql_insert = """insert into barbearia (nome, telefone, endereco, forma_pagamento) 
                        values (%s, %s, %s, %s)"""
    dados   = (nome, telefone, endereco, forma_pagamento)
    cursor.execute(sql_insert, dados)
    conexao.commit()
        
def alterar_barbearia_bd(conexao, id, nome,telefone,endereco,forma_pagamento):
    cursor = conexao.cursor()
    sql_update = """update barbearia set nome= %s, telefone = %s, endereco = %s, forma_pagamento= %s
                   where id = %s"""
    # Id e o último campo a ser passado para o array de dados 
    dados   = (nome, telefone, endereco,forma_pagamento, id)
    cursor.execute(sql_update, dados)
    conexao.commit()


def buscar_barbearia_por_id_bd(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("""
            select id, nome, telefone, endereco, forma_pagamento
            from barbearia
            where id = %s
        """, (id,))
    registro = cursor.fetchone()
    return registro


