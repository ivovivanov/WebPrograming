from models import userdb
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Welsome to our First Web App"

@app.route('/users')
def users():
    return render_template('users.html', n1 = userdb.f_names[0], n2 = userdb.f_names[1], f1 = userdb.l_names[0], f2 = userdb.l_names[1])

@app.route('/about')
def about():
    render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)