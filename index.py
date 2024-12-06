import pymysql
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "smakonakl0ioe8390732890dshui"

# Simulação de dados (sem conexão com MySQL)
clientes = [
    {"id": 1, "nome": "João", "email": "joao@example.com"},
    {"id": 2, "nome": "Maria", "email": "maria@example.com"}
]

# Função que simula a atualização dos dados
def atualizar_cliente(id, nome, email):
    for cliente in clientes:
        if cliente["id"] == int(id):
            cliente["nome"] = nome
            cliente["email"] = email
            break

# Função que simula a inserção de dados
def inserir_cliente(nome, email):
    novo_id = max(cliente["id"] for cliente in clientes) + 1
    clientes.append({"id": novo_id, "nome": nome, "email": email})

# Função que simula a exclusão de um cliente
def deletar_cliente(id):
    global clientes
    clientes = [cliente for cliente in clientes if cliente["id"] != int(id)]

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Garantir que o valor de 'id' não seja vazio antes de convertê-lo para inteiro (para atualizar)
        id = request.form.get('id')
        if id == '' or id is None:
            flash("ID não pode ser vazio", "error")
            return redirect("/")
        
        try:
            id = int(id)  # Converte para inteiro
        except ValueError:
            flash("ID deve ser um número válido", "error")
            return redirect("/")

        nome = request.form.get('nome')
        email = request.form.get('email')

        if not nome or not email:
            flash("Nome e email são obrigatórios", "error")
            return redirect("/")
        
        # Simula a atualização de cliente
        atualizar_cliente(id, nome, email)

        flash("Cliente atualizado com sucesso!", "success")
        return redirect("/")
    else:
        # Retorna os dados simulados
        return render_template("index.html", content=clientes)


@app.route("/inserir", methods=['POST'])
def inserir():
    nome = request.form.get('nome')
    email = request.form.get('email')

    if not nome or not email:
        flash("Nome e email são obrigatórios", "error")
        return redirect("/")

    # Simula a inserção de cliente
    inserir_cliente(nome, email)
    
    flash("Cliente inserido com sucesso!", "success")
    return redirect("/")


@app.route("/deletar", methods=['POST'])
def deletar():
    id = request.form.get('id')

    # Verificar se o ID é válido antes de realizar a exclusão
    if id == '' or id is None:
        flash("ID não pode ser vazio", "error")
        return redirect("/")
    
    try:
        id = int(id)
    except ValueError:
        flash("ID deve ser um número válido", "error")
        return redirect("/")
    
    # Simula a exclusão de um cliente
    deletar_cliente(id)

    flash("Cliente deletado com sucesso!", "success")
    return redirect("/")


@app.route("/sobre")
def sobre():
    return "<h2>Sobre</h2>"


@app.route("/noticia/<noticia_slug>")
def noticia(noticia_slug):
    return "Noticia: " + noticia_slug


if __name__ == "__main__":
    app.run(debug=True)
