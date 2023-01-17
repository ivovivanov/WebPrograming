import flask.cli
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Welsome to our First Web App"

@app.route('/users')
def users():
    return render_template('users.html')


if __name__ == '__main__':
    app.run(debug=True)