from flask import Flask, render_template, request
from models.aws_db import db_inst_types

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        db_search_criteria = request.form["search_string"]
        dbs = list()
        for db in db_inst_types:
            if db_search_criteria in db.get('type'):
                dbs.append(db)
        return render_template('search.html', dbs=dbs)
    else:
        return render_template('search.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)
