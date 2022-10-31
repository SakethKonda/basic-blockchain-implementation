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

@app.route('/home')
def show_home():
	return render_template("home.html")

@app.route('/blockchain')
def print_blockchain():
	result = blockchain.return_blockchain(2)
	return render_template('data.html',result=result)

@app.route('/input',methods = ['GET','POST'])
def input():
	form = InputData()
	if form.is_submitted():
		data = request.form
		data = dict(data)
		blockchain.add_new([data])
		result = blockchain.mine()
		return render_template('result.html',query = 'Status for Addition of data : ',status=result)
	return render_template('input.html',form=form)

@app.route('/search',methods=['GET','POST'])
def search():
	form = InputData()
	if form.is_submitted():
		data = request.form
		uidx = str(data['uidx'])
		result = blockchain.return_data(uidx)
		return render_template('result.html',query = f'Search status : ',status=result)
	return render_template('search_input.html',form=form)

with open('test_data.csv','r') as f:
	dict_reader = csv.DictReader(f)
	data = list(dict_reader)
blockchain = Blockchain()
blockchain.add_new(data)
blockchain.mine()
result = blockchain.return_blockchain(2)

app.run()