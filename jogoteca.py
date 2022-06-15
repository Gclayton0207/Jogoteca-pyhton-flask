from flask import Flask, render_template


class Jogo:
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma


app = Flask(__name__)


@app.route('/inicio')
def ola():
    Jogo1 = Jogo('Counter-Strike', 'FPS', 'PC')
    Jogo2 = Jogo('Pokemon', 'RPG', 'Nintendo Switch')
    Jogo3 = Jogo ('Forza', 'Corrida', 'Xbox')
    listaDeJogos = [Jogo1, Jogo2, Jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=listaDeJogos)


app.run()
