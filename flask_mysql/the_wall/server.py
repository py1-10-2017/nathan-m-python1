from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'super_secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app, 'the_walldb')
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user' not in session:
        return render_template('index.html')
    else:
        return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
	logemail = request.form['logemail']
	logpw = request.form['logpw']
	error = False	

	if len(logemail) == 0:
	 	flash('Email required')
	 	error = True	

	if not len(logemail) == 0 and not EMAIL_REGEX.match(logemail):
	 	flash('Email address not in proper format')
	 	error = True

	if error:
		return redirect('/')

	if not error:
		try:
		 	query = "SELECT * FROM users WHERE email = '%s' " % (logemail)
		 	user = mysql.query_db(query)
		 	
		 	if bcrypt.check_password_hash(user[0]['pw_hash'], logpw):
		 		session['user_id'] = user[0]['id']
		 		return redirect('/wall')	
			else:
				flash("Incorrect Password")	
				return redirect('/')

		except (IndexError):
			flash('Email address is not registered.') 
			return redirect('/')	

@app.route('/create_user', methods=['POST'])
def create_user():
	fname = request.form['fname']
	lname = request.form['lname']
	email = request.form['email']
	pword = request.form['pword']
	pwconfirm = request.form['pwconfirm']
 	
	error = False

	if len(fname) == 0:
		flash('First Name required')
		error = True

	if len(fname) < 2:
		flash('First Name must be more than 2 characters')
		error = True
		
	if not len(fname) != 0 and not fname.isalpha():
		flash('First Name must be letters only')
		error = True

	if len(lname) == 0:
		flash('Last Name required')
		error = True					

	if len(lname) < 2:
		flash('Last Name must be more than 2 characters')
		error = True
		
	if not len(lname) != 0 and not lname.isalpha():
		flash('Last Name must be letters only') 
		error = True		

	if len(email) == 0:
		flash('Email required')
		error = True		

	if not len(email) == 0 and not EMAIL_REGEX.match(email):
		flash('Email address not valid')
		error = True	

	if len(pword) == 0:
		flash('Password required')
		error = True

	if len(pword) < 8:
		flash('Password must be at least 8 characters')
		error = True

	if pwconfirm != pword:
		flash('Password and Confirm Password must match')
		error = True
			
	if error:
		return redirect('/')
		
	if not error:
		pw_hash = bcrypt.generate_password_hash(pword)
		flash('Registration successful')	
		query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:fname, :lname, :email, :pw_hash, NOW(), NOW())"

		data = 	{
					'fname': fname,
					'lname': lname,
					'email': email,
					'pw_hash': pw_hash
				}

		mysql.query_db(query, data)
			
		return redirect('/')

@app.route('/wall')
def success ():
	user_id = session['user_id']
	query1 = "SELECT users.id AS user_id, first_name, last_name, messages.id AS message_id, message, comment, comments.created_at AS comment_created, comments.message_id AS commessage_id, comments.user_id AS comuser_id FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON comments.user_id = users.id;"
	user1 = mysql.query_db(query1)	

	query2 = "SELECT users.id AS user_id, first_name, last_name, messages.created_at AS message_created, messages.id AS message_id, message FROM users JOIN messages ON users.id = messages.user_id;"
	user2 = mysql.query_db(query2)

	query3 = "SELECT * FROM users WHERE id = {};".format(user_id)
	user3 = mysql.query_db(query3)

	return render_template('wall.html', user1=user1, user2=user2, user3=user3, user_id=user_id)

@app.route('/wall/<user_id>/message', methods=['POST'])
def message (user_id):
	message = request.form['message']	
	query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), '%s')" % (user_id)
	data = 	{
				'message': message,
			}
	mysql.query_db(query, data)
	
	return redirect('/wall')

@app.route('/wall/<message_id>/<user_id>/comment', methods=['POST'])
def comment (message_id, user_id):
	comment = request.form['comment']	
	query = "INSERT INTO comments (comment, created_at, updated_at, user_id, message_id) VALUES (:comment, NOW(), NOW(), '{}', '{}')".format(session['user_id'], message_id)
	print query
	data = 	{
				'comment': comment,
			}
	mysql.query_db(query, data)
	
	return redirect('/wall')	

@app.route('/log_off')
def log_off():
	session.pop('user_id')
	return redirect('/')

app.run(debug=True)