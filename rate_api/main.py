from flask import Flask, jsonify
import models.items


app = Flask(__name__)


@app.route('/')
def rate():
    items = models.items.get_items()
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True, port=5002)

