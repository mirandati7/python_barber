from bd.conexao import conecta_db
import bcrypt

def listar_clientes_bd(conexao):
    cursor = conexao.cursor()
    # Execução do select no banco de dados
    cursor.execute("select id,nome,sexo,telefone,observacao from cliente order by id asc")
    # recuperar todos registros
    registros = cursor.fetchall()
    return registros


def consultar_cliente_por_id(conexao):
    cursor = conexao.cursor()
    cursor.execute("select id,nome from cliente where id = " + id)
    registro = cursor.fetchone()

    if registro is None:
        print("Cliente não encontrado:")
    else:
        print(f"| ID ..: {registro[0]} ")
        print(f"| Nome : {registro[1]} ")


def inserir_cliente_bd(conexao, nome,sexo, telefone,senha,observacao):
    cursor = conexao.cursor()

    senha = senha.encode('utf-8')
    salt = bcrypt.gensalt() #Gera um salt aleatorio
    hash_senha = bcrypt.hashpw(senha, salt)
    print("Hash Senha ", hash_senha)

    print("Inserindo o Cliente ..: ")
    sql_insert = "insert into cliente (nome,sexo,telefone,senha,observacao) values ( %s,%s, %s,%s,%s)"
    dados = (nome,sexo,telefone,hash_senha.decode('utf-8'),observacao)
    cursor.execute(sql_insert,dados)
    conexao.commit()

def atualizar_cliente_bd(conexao):
    print("Alterando dados dos Cliente")
    cursor = conexao.cursor()
    id   = input("Digite o ID : ")
    nome = input("Nome :")
    sql_update = "update cliente set nome ='" + nome + "' where id = "+ id
    cursor.execute(sql_update)
    conexao.commit()

def deletar_cliente_bd(conexao):
    print("Deletando Cliente")
    cursor = conexao.cursor()
    id   = input("Digite o ID : ")
    sql_delete = "delete from cliente where id = "+ id
    cursor.execute(sql_delete)
    conexao.commit()
