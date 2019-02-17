from flask import Flask
from flask_restful import Resource, Api, reqparse
from language_processing.process_text import syntax_text
import os

flask_debug = os.getenv('FLASK_DEBUG', True)

app = Flask(__name__)
api = Api(app)

post_parser = reqparse.RequestParser()
post_parser.add_argument('pasta_text', dest='pasta_text', required=True)


class CopyPasta(Resource):
    def post(self):
        args = post_parser.parse_args()
        pasta_text = args.pasta_text
        unicode_text = pasta_text.encode('utf-8').decode('utf-8')
        tokenized_text = syntax_text(unicode_text)
        return unicode_text

    def get(self):
        return '{"hello": "world}'


api.add_resource(CopyPasta, '/pasta_text')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
