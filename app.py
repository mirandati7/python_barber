from flask  import Flask,render_template, request, redirect,url_for,jsonify, session
from functools import wraps

from bd.conexao import conecta_db
from bd.barbearia_bd import inserir_barbearia_bd, listar_barbearia_bd,alterar_barbearia_bd,buscar_barbearia_por_id_bd
from bd.cliente_bd import inserir_cliente_bd, listar_clientes_bd ,consultar_cliente_por_id_bd, atualizar_cliente_bd
from bd.profissionais_bd import inserir_profissionais_bd, listar_profissionais_bd
from bd.servico_bd import inserir_servicos_bd, listar_servicos_bd
from bd.login_bd import login_profissional_bd, login_cliente_bd
from bd.agendamento_bd import listar_agendamentos_db, inserir_agendamento_bd

from routes.barbearia import barbearias

app = Flask(__name__)
app.secret_key = "designcursos"

app.register_blueprint(barbearias)

## Login Required do Admin
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "usuario_logado" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


def login_required_cliente(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "cliente_logado" not in session:
            return redirect(url_for("login_cliente"))
        return f(*args, **kwargs)
    return decorated


@app.route('/home')
def home():
    nome = "Sistema de Barbearia"
    return render_template("home.html",nome=nome)


@app.route('/area-cliente')
def area_cliente():
    nome = "Sistema de Barbearia Àrea do cliente"
    return render_template("area_cliente.html",nome=nome)







@app.route("/agendamentos/listar", methods=['GET','POST'])
@login_required
def agendamento_listar():
    conexao = conecta_db()
    agendamentos = listar_agendamentos_db(conexao)
    return render_template("agendamento_listar.html",agendamentos=agendamentos)



@app.route("/agendamentos/novo", methods=['GET','POST'])
@login_required_cliente
def salvar_agendamento():
    conexao = conecta_db()
    barbeiros = listar_profissionais_bd(conexao)
    servicos = listar_servicos_bd(conexao)

    if request.method == 'POST':
        id_cliente = request.form.get('id_cliente')
        id_profissional = request.form.get('id_profissional')
        id_servico = request.form.get('id_servico')
        data_hora = request.form.get('data_hora')
        valor_servico = request.form.get('valor_servico')
        status = request.form.get('status')
        print("Teste de Cadastro de Agendamentos ")
        inserir_agendamento_bd(conexao,id_cliente,id_profissional, id_servico,data_hora,valor_servico,status)   

        return f"<h2> Agendamento Salvo com Sucesso:  </h2>"
    
    return render_template("agendamento_form.html",barbeiros=barbeiros,servicos=servicos)


@app.route("/clientes/listar", methods=['GET','POST'])
@login_required
def cliente_listar():
    conexao = conecta_db()
    clientes = listar_clientes_bd(conexao)
    return render_template("cliente_listar.html",clientes=clientes)

@app.route("/clientes/novo", methods=['GET','POST'])
@login_required
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



@app.route("/clientes/<int:id>/editar", methods=['GET','POST'])
@login_required
def cliente_editar(id):
    conexao = conecta_db()
    if request.method == "GET":
        cliente = consultar_cliente_por_id_bd(conexao, id)

        if not cliente:
            return "<h3> Cliente não encontrado </h3"
        return render_template("cliente_editar.html", cliente=cliente)


    nome = request.form.get('nome')
    sexo = request.form.get('sexo')
    telefone = request.form.get('telefone')
    observacao = request.form.get('observacao')

    atualizar_cliente_bd(conexao,nome,sexo, telefone,observacao,id)

    return "<h3> Cliente Salvo com sucesso </h3"



@app.route("/profissionais/listar", methods=['GET','POST'])
@login_required
def profissional_listar():
    conexao = conecta_db()
    profissionais = listar_profissionais_bd(conexao)
    return render_template("profissional_listar.html",profissionais=profissionais)

@app.route("/profissionais/novo", methods=['GET','POST'])
@login_required
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
@login_required
def servico_listar():
    conexao = conecta_db()
    servicos = listar_servicos_bd(conexao)
    return render_template("servico_listar.html",servicos=servicos)

@app.route("/servicos/novo", methods=['GET','POST'])
@login_required
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



@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        # Valida campos obrigatórios; ajuste aqui para autenticar de verdade
        if not usuario or not senha:
            erro = "Preencha usuário e senha para entrar."
            return render_template("login.html", erro=erro)
        
        conexao = conecta_db()
        valida_login = login_profissional_bd(conexao,usuario, senha)
        # Antes de redirecionar vamos fazer a validação do usuario e senha

        if valida_login == "OK":
            session["usuario_logado"] = usuario
            return redirect(url_for('home'))
        else:
            return render_template("login.html",erro=valida_login)
        
    # Obriga a passar no login.html    
    return render_template("login.html")


@app.route('/login', methods=['GET','POST'])
def login_cliente():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        # Valida campos obrigatórios; ajuste aqui para autenticar de verdade
        if not usuario or not senha:
            erro = "Preencha usuário e senha para entrar."
            return render_template("login_cliente.html", erro=erro)
        
        conexao = conecta_db()
        valida_login = login_cliente_bd(conexao,usuario, senha)
        # Antes de redirecionar vamos fazer a validação do usuario e senha

        if valida_login == "OK":
            session["cliente_logado"] = usuario
            return redirect(url_for('area_cliente'))
        else:
            return render_template("login_cliente.html",erro=valida_login)
        
    # Obriga a passar no login.html    
    return render_template("login_cliente.html")


@app.route("/logout")
def logout():
    session.pop("usuario_logado", None)
    return redirect(url_for("login"))


@app.route("/logout-cliente")
def logout_cliente():
    session.pop("cliente_logado", None)
    return redirect(url_for("login_cliente"))


if __name__ == "__main__":
    app.run(debug=True)






# print("Projeto Barbearia")

# conexao  = conecta_db()
# inserir_barbearia_bd(conexao,"BARBER 10","48991779063","BR 470", "PIX")
# print("Registro inserido com sucesso")