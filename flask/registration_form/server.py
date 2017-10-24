from flask import Flask, render_template, request, flash, redirect, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')

def index():
  return render_template("index.html")

@app.route('/check', methods=['POST'])

def check():
	error = False

	if len(request.form['email']) == 0:
		flash('Email required')
		error = True	

	if not len(request.form['email']) == 0 and not EMAIL_REGEX.match(request.form['email']):
		flash('Email address not valid')
		error = True			

	if len(request.form['first_name']) == 0:
		flash('First Name required')
		error = True

	if not len(request.form['first_name']) == 0 and not request.form['first_name'].isalpha():
		flash('First Name must be letters only')
		error = True			

	if len(request.form['last_name']) == 0:
		flash('Last Name required')
		error = True

	if not len(request.form['last_name']) == 0 and not request.form['last_name'].isalpha():
		flash('Last Name must be letters only')
		error = True				

	if len(request.form['password']) == 0:
		flash('Password required')
		error = True

	if not len(request.form['password']) == 0 and len(request.form['password']) < 8:
		flash('Password must be more than 8 characters')
		error = True

	if len(request.form['confirmpw']) == 0:
		flash('Password Confirmation required')
		error = True

	if not len(request.form['confirmpw']) == 0 and request.form['confirmpw'] != (request.form['password']):
		flash('Confirm Password must match Password')
		error = True				

	if not error:
		flash("Thank you for submitting your registration.")

	return redirect('/')

app.run(debug=True)