from models import userdb
from models import pass_lib
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to our First Web App"

@app.route('/users')
def users():
    return render_template('users.html', n1 = userdb.f_names[0], n2 = userdb.f_names[1], f1 = userdb.l_names[0], f2 = userdb.l_names[1])

@app.route('/about')
def about():
    return render_template('about.html')

#We want a page that will genarate random 10 character password. If choice is 0 - only letters, choice is 1 - letters and nubers, choice 2 letters numbers and special chars

@app.route('/generate_pass/<int:choice>/<plen>')
def generate(choice, plen):
    if choice in [0, 1, 2]:
        generate_pass=pass_lib.passlib.gen_pass(choice, plen)
        return render_template('password.html', genpass=generate_pass[0], passlen=generate_pass[1])
    else:
        return render_template('password.html')


if __name__ == '__main__':
    app.run(debug=True)