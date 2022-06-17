from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy


class Jogo:
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma


Jogo1 = Jogo('Counter-Strike', 'FPS', 'PC')
Jogo2 = Jogo('Pokemon', 'RPG', 'Nintendo Switch')
Jogo3 = Jogo('Forza', 'Corrida', 'Xbox')
listaDeJogos = [Jogo1, Jogo2, Jogo3]


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


usuario1 = Usuario("Giovanni Clayton", "Gclayton", "alohomora")
usuario2 = Usuario("Juliana Melo", "Juuh", "alohomora")
usuario3 = Usuario("Batolomeu", "Barto", "jade")

usuarios = {usuario1.nickname: usuario1,
            usuario2.nickname: usuario2,
            usuario3.nickname: usuario3}

app = Flask(__name__)
app.secret_key = 'claytinho'

app.config['SQLAlCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'number1245',
        server = 'localhost',
        database = 'jogoteca'
    )

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=listaDeJogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    plataforma = request.form['plataforma']
    jogo = Jogo(nome, categoria, plataforma)
    listaDeJogos.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)
