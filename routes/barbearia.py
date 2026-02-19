from flask  import  Blueprint,render_template, request, redirect,url_for,jsonify, session
from functools import wraps
from auth import login_required
from bd.conexao import conecta_db
from bd.barbearia_bd import inserir_barbearia_bd, listar_barbearia_bd,alterar_barbearia_bd,buscar_barbearia_por_id_bd

barbearias = Blueprint("barbearias", __name__, url_prefix="/barbearias")

@barbearias.route("/novo", methods=['GET','POST'], endpoint="novo")
@login_required
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


@barbearias.route("/listar", methods=['GET','POST'], endpoint="listar")
@login_required
def barbearia_listar():
    conexao = conecta_db()
    barbearias = listar_barbearia_bd(conexao)
    return render_template("barbearia_listar.html",barbearias=barbearias)


@barbearias.route("/barbearias/<int:id>/editar", methods=["GET", "POST"], endpoint="editar")
@login_required
def barbearia_editar(id):
    conexao = conecta_db()

    if request.method == "GET":
        barbearia = buscar_barbearia_por_id_bd(conexao, id)
        if not barbearia:
            return "<h3> Barbearia não encontrada </h3"
        return render_template("barbearia_editar.html", barbearia=barbearia)

    # POST
    nome = request.form.get("nome", "").strip()
    telefone = request.form.get("telefone", "").strip()
    endereco = request.form.get("endereco", "").strip()
    forma_pagamento = request.form.get("forma_pagamento", "").strip()

    alterar_barbearia_bd(conexao, id, nome, telefone, endereco, forma_pagamento)
    return redirect(url_for("barbearias.listar"))