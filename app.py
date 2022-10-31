from flask import Flask, render_template, request
from util import *
from blocks import Block
from blockchain import Blockchain
from forms import InputData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fet_grp_3_blockchain'

@app.route("/")
def home():
	return render_template("home.html")

@app.route('/input',methods = ['GET','POST'])
def input():
	form = InputData()
	if form.is_submitted():
		result = request.form
		print(type(result))
		print(result)
	return render_template('input.html',form=form)

with open('test_data.csv','r') as f:
	dict_reader = csv.DictReader(f)
	data = list(dict_reader)
blockchain = Blockchain()
blockchain.add_new(data)
blockchain.mine()
result = blockchain.return_blockchain(2)

@app.route('/blockchain')
def print_blockchain():
	return format_string_for_html(result)

app.run()