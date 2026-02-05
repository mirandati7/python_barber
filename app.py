from flask  import Flask,render_template, request, redirect,url_for,jsonify 

from bd.conexao import conecta_db
from bd.barbearia_bd import inserir_barbearia_bd, listar_barbearia_bd
from bd.cliente_bd import inserir_cliente_bd, listar_clientes_bd
from bd.profissionais_bd import inserir_profissionais_bd, listar_profissionais_bd
from bd.servico_bd import inserir_servicos_bd, listar_servicos_bd

app = Flask(__name__)

@app.route('/home')
def home():
    nome = "Sistema de Barbearia"
    return render_template("home.html",nome=nome)


@app.route("/barbearias/novo", methods=['GET','POST'])
def salvar_barbearia():
    if request.method == 'POST':
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        forma_pagamento = request.form.get('forma_pagamento')

        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3"
        
        conexao = conecta_db()
        inserir_barbearia_bd(conexao,nome,telefone,endereco,forma_pagamento)

        return f"<h2> Barbearia Salvo com Sucesso:  {nome} </h2>"
    return render_template("barbearia_form.html",titulo="Barbearias")


@app.route("/barbearias/listar", methods=['GET','POST'])
def barbearia_listar():
    conexao = conecta_db()
    barbearias = listar_barbearia_bd(conexao)
    return render_template("barbearia_listar.html",barbearias=barbearias)


@app.route("/clientes/listar", methods=['GET','POST'])
def cliente_listar():
    conexao = conecta_db()
    clientes = listar_clientes_bd(conexao)
    return render_template("cliente_listar.html",clientes=clientes)

@app.route("/clientes/novo", methods=['GET','POST'])
def salvar_cliente():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sexo = request.form.get('sexo')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')
        observacao = request.form.get('observacao')
        print("Teste de Cadastro de Clientes")

        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3"
        
        conexao = conecta_db()
        inserir_cliente_bd(conexao,nome,sexo, telefone,senha,observacao)

        return f"<h2> Cliente Salvo com Sucesso:  {nome} </h2>"
    return render_template("cliente_form.html")


@app.route("/profissionais/listar", methods=['GET','POST'])
def profissional_listar():
    conexao = conecta_db()
    profissionais = listar_profissionais_bd(conexao)
    return render_template("profissional_listar.html",profissionais=profissionais)

@app.route("/profissionais/novo", methods=['GET','POST'])
def salvar_profissional():
    if request.method == 'POST':
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')
       
        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3>"
        
        conexao = conecta_db()
        inserir_profissionais_bd(conexao,nome,telefone,senha)

        return f"<h2> Profissional Salvo com Sucesso:  {nome} </h2>"
    return render_template("profissional_form.html")

@app.route("/servicos/listar", methods=['GET','POST'])
def servico_listar():
    conexao = conecta_db()
    servicos = listar_servicos_bd(conexao)
    return render_template("servico_listar.html",servicos=servicos)

@app.route("/servicos/novo", methods=['GET','POST'])
def salvar_servico():
    if request.method == 'POST':
        nome = request.form.get('nome')
        tempo_estimado = request.form.get('tempo_estimado')
        valor_estimado = request.form.get('valor_estimado')
       
        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3>"
        
        conexao = conecta_db()
        inserir_servicos_bd(conexao,nome,tempo_estimado,valor_estimado)

        return f"<h2> Serviço Salvo com Sucesso:  {nome} </h2>"
    return render_template("servico_form.html")



if __name__ == "__main__":
    app.run(debug=True)






# print("Projeto Barbearia")

# conexao  = conecta_db()
# inserir_barbearia_bd(conexao,"BARBER 10","48991779063","BR 470", "PIX")
# print("Registro inserido com sucesso")