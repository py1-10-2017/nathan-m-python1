from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'super_secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app, 'friends1db')

@app.route('/')
def index ():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	fname = request.form['fname']
	lname = request.form['lname']
	email = request.form['email']
	error = False

	if len(fname) == 0:
		flash('First Name required')
		error = True
		
	if not len(fname) == 0 and not fname.isalpha():
		flash('First Name must be letters only')
		error = True				

	if len(lname) == 0:
		flash('Last Name required')
		error = True
		
	if not len(lname) == 0 and not lname.isalpha():
		flash('Last Name must be letters only') 
		error = True		

	if len(email) == 0:
		flash('Email required')
		error = True		

	if not len(email) == 0 and not EMAIL_REGEX.match(email):
		flash('Email address not valid')
		error = True
			
	if error:
		return redirect('/')
		
	if not error:	
		query = "INSERT INTO friends (first_name, last_name, email_address, created_at, updated_at) VALUES (:fname, :lname, :email, NOW(), NOW())"

		data = 	{
					'fname': fname,
					'lname': lname,
					'email': email
				}

		mysql.query_db(query, data)
			
		return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM friends WHERE id =" + id
	friend =  mysql.query_db(query)

	return render_template('edit.html', this_friend=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	firstn = request.form['firstn']
	lastn = request.form['lastn']
	email1 = request.form['email1']
	error = False

	if len(firstn) == 0:
		flash('First Name required')
		error = True

	if not len(firstn) == 0 and not firstn.isalpha():
		flash('First Name must be letters only')
		error = True			

	if len(lastn) == 0:
		flash('Last Name required')
		error = True

	if not len(lastn) == 0 and not lastn.isalpha():
		flash('Last Name must be letters only') 
		error = True	

	if len(email1) == 0:
		flash('Email required')
		error = True	

	if not len(email1) == 0 and not EMAIL_REGEX.match(email1):
		flash('Email address not valid')
		error = True

	if error:
		return redirect('/friends/' + id + '/edit')
	if not error:
		query = "UPDATE friends SET first_name = :firstn, last_name = :lastn, email_address = :email1 WHERE id =" + id 

		data = 	{
					'firstn': firstn,
					'lastn': lastn,
					'email1': email1
				}

		mysql.query_db(query, data)
				
		return redirect('/')

@app.route('/friends/<id>/delete')
def destroy(id):
	query = "DELETE FROM friends WHERE id =" + id

	data = 	{

				'id': id
			}

	mysql.query_db(query, data)
			
	return redirect('/')


app.run(debug=True)