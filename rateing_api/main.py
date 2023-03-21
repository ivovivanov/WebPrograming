from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
rating_api = Api(app)

class rating(Resource):
    def get(self):
        return {'rating': 5}

rating_api.add_resource(rating, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
