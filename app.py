from flask import Flask, render_template
from flask import request
import sqlite3 

app=Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')
@app.route('/Order', methods=['GET','POST'])
def Order():
	if request.method == 'POST':
		connection=sqlite3.connect('coffeebot_db.db')
		cursor=connection.cursor()
		ordername=request.form.get('rname')
		orderprice=request.form.get('remail')
	return render_template('Order.html')

@app.route('/Regstr', methods=['GET','POST'])
def Regstr():
	if request.method == 'POST':
		connection=sqlite3.connect('coffeebot_db.db')
		cursor=connection.cursor()
		name=request.form.get('rname')
		email=request.form.get('remail')
		password=request.form.get('rpass')
		repassword=request.form.get('repass')
		numb=request.form.get('rnum')
		
		try:
			cursor.execute('INSERT INTO users(name,email,password,repassword,numb) VALUES(?,?,?,?,?)',(name,email,password,repassword,numb))
			connection.commit()
			message='success'
		except:
			connection.rollback()
			message='failure'
		finally:
			connection.close()
			return message
	return render_template('Regstr.html')	

if __name__=='__main__':
	app.run()