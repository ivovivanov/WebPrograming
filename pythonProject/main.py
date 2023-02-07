from flask import Flask, render_template
from models.nav import navbar
from models.generator import gen_password
from models.inventory import books, get_book_isbn

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', menu=navbar)


@app.route('/books')
def get_books():
    return render_template('books.html', menu=navbar, inventory=books)


@app.route('/book/<isbn>')
def get_book(isbn):
    return render_template('book.html', menu=navbar, book=get_book_isbn(isbn))


@app.route('/pass_gen')
def pass_gen():
    return render_template('pass_gen.html', menu=navbar, passwd=gen_password())



if __name__ == '__main__':
    app.run(debug=True)
