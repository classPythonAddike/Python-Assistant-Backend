from flask import Flask
from flask_restful import Api, reqparse, Resource
from helper_mod import get_code_compl
from PIL import ImageTk, Image
from tkinter import Tk, Label, Button, messagebox
import requests

data_parser = reqparse.RequestParser()
data_parser.add_argument("Code", type = str, help = "The last character typed", required = True)
data_parser.add_argument("Index", type = int, help = "Cursors position", required = True)

app = Flask(__name__)
api = Api(app)

class CodeCompleter(Resource):

	def get(self):
		args = data_parser.parse_args()
		return get_code_compl(args["Code"], args["Index"]), 200

class CheckIfReady(Resource):
	def get(self):
		return "OK", 200

api.add_resource(CodeCompleter, "/api")
api.add_resource(CheckIfReady, "/check")

class ui():
	def __init__(self):
		self.root = Tk()
		self.icn = ImageTk.PhotoImage(Image.open("image.png"))
		self.root.title("Python Assistant")
		self.root.iconbitmap('icon.ico')
		self.root.resizable(False, False)
		self.b1 = Button(self.root, image = self.icn, command = self.show_info)
		self.b1.grid(row = 0, column = 0)
		self.root.configure(width = 340, height = 450, bg = "lightblue")
		self.to_run = False
		self.root.wm_withdraw()
		self.show_ui()

	def show_info(self):
		try:
			h = requests.get("http://127.0.0.1:5555/check/")
			m = messagebox.showinfo("Python Assistant", "The Assistant is already with you. The backend is already running!")
			self.to_run = False
		except:
			m = messagebox.showinfo("Python Assistant", "The backend has started up! May the Assistant go with you!")
			self.to_run = True
		self.root.destroy()

	def show_ui(self):
		self.show_info()
		self.root.mainloop()

r = ui()
if r.to_run:
	app.run(debug=False, port=5555)