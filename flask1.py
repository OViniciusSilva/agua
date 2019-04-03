from flask import Flask, render_template
from classedoflask import Pessoa

app = Flask(__name__)

pessoas = [
        Pessoa("Tim","Polifonia","3241"),
        Pessoa("Kalebe", "3Portas", "123"),
        Pessoa("john", "latifundio", "12335"),
        Pessoa("Joe", "canetacity", "12453")
    ]


@app.route("/")
def inicio ():
    return render_template('inicio.html')


@app.route("/listar_pessoas.html")
def listar_pessoas():
    return render_template("listar_pessoas.html", lista = pessoas)


@app.route("/form_inserir_pessoas.html")
def form_inserir_pessoas ():
	return render_template('form_inserir_pessoas.html')


@app.route("/form_alterar_pessoa.html")
def form_alterar_pessoa():
	return render_template('form_alterar_pessoa.html')


@app.route("/exibir_mensagem.html")
def exibir_mensagem():
	return render_template('exibir_mensagem.html')





app.run(debug=True)