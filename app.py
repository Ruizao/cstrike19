from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobreojg')
def sobreojg():
    return render_template('sobreojg.html')

@app.route('/modo')
def modo():
    return render_template('modo.html')

@app.route('/casual')
def casual():
    return render_template('casual.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/logar')
def logar():
    return render_template('logar.html')

@app.route('/esports')
def esports():
    return render_template('esports.html')

@app.route('/competitivo')
def competitivo():
    return render_template('competitivo.html')

@app.route('/skins')
def skins():
    return render_template('skins.html')

@app.route('/criar')
def criar():
    return render_template('criar.html')

@app.route('/galo')
def galo():
    return render_template('galo.html')

@app.route('/perifericos')
def perifericos():
    return render_template('perifericos.html')

@app.route('/wingman')
def wingman():
    return render_template('wingman.html')

if __name__ == '__main__':
    app.run(debug=True)
