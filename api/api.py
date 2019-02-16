from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

post_parser = reqparse

class CopyPasta(Resource):
    def get(self):
        args =
        return {'hello': 'world'}

    def post(self):
        return


api.add_resource(CopyPasta, '/')


if __name__ == '__main__':
    app.run(debug=True)
