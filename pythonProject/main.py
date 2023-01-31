from flask import Flask, render_template
from models.nav import navbar
from models.generator import gen_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', menu=navbar)

@app.route('/books')
def get_books():
    return render_template('users.html', menu=navbar)

@app.route('/pass_gen')
def pass_gen():
    return render_template('pass_gen.html', menu=navbar, passwd=gen_password())



if __name__ == '__main__':
    app.run(debug=True)
