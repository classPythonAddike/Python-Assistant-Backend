from flask import Flask
from flask_restful import Api, reqparse, Resource
from helper_mod import get_code_compl

data_parser = reqparse.RequestParser()
data_parser.add_argument("Code", type = str, help = "Full Python Program", required = True)
data_parser.add_argument("Index", type = int, help = "Cursors position", required = True)

app = Flask(__name__)
api = Api(app)

class CodeCompleter(Resource):

	def get(self):
		args = data_parser.parse_args()
		return get_code_compl(args["Code"], args["Index"]), 200

api.add_resource(CodeCompleter, "/api")

if __name__ == "__main__":
	app.run(debug=True)