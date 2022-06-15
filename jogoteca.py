from flask import Flask, render_template;

app = Flask(__name__)

@app.route('/inicio')
def ola():
    listaDeJogos = ['CS','Overwatch','GTA']
    return render_template('lista.html', titulo='Jogos', jogos=listaDeJogos)

app.run()