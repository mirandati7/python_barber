from bd.conexao import conecta_db

def listar_servicos_bd(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
              select id,nome,tempo_estimado,valor_servico
              from servico order by id asc""")
    registros = cursor.fetchall()
    return registros


def inserir_servicos_bd(conexao, nome,tempo_estimado,valor_servico):
    cursor = conexao.cursor()
    sql_insert = """insert into servico (nome,tempo_estimado,valor_servico) 
                        values (%s, %s, %s)"""
    dados   = (nome,tempo_estimado,valor_servico)
    cursor.execute(sql_insert, dados)
    conexao.commit()
        
def alterar_servicos_bd(conexao, id, nome,tempo_estimado,valor_servico):
    cursor = conexao.cursor()
    sql_update = """update servico set nome= %s, tempo_estimado = %s, valor_servico = %
                   where id = %s"""
    # Id e o último campo a ser passado para o array de dados 
    dados   = ( nome,tempo_estimado,valor_servico, id)
    cursor.execute(sql_update, dados)
    conexao.commit()


