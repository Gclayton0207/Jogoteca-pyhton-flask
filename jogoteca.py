from flask import Flask, render_template, request, redirect


class Jogo:
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma


Jogo1 = Jogo('Counter-Strike', 'FPS', 'PC')
Jogo2 = Jogo('Pokemon', 'RPG', 'Nintendo Switch')
Jogo3 = Jogo('Forza', 'Corrida', 'Xbox')
listaDeJogos = [Jogo1, Jogo2, Jogo3]

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('lista.html', titulo='Jogos', jogos=listaDeJogos)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    plataforma = request.form['plataforma']
    jogo = Jogo(nome, categoria, plataforma)
    listaDeJogos.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True)
