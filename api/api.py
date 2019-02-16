from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

post_parser = reqparse.RequestParser()
post_parser.add_argument('pasta_text', dest='pasta_text', location='form', required=True)


class CopyPasta(Resource):
    def post(self):
        args = post_parser.parse_args()
        pasta_text = args.pasta_text
        unicode_text = pasta_text.encode('utf-8')
        return unicode_text


api.add_resource(CopyPasta, '/')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
