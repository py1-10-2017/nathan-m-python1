from flask import Flask, redirect, request, render_template, flash, session
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
app.secret_key = 'super_secret'

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/add', methods=['POST'])
def check():
    error = False
    
    if len(request.form['email']) == 0:
        flash('Email required')
        error = True 
        return redirect('/')

    if not len(request.form['email']) == 0 and not EMAIL_REGEX.match(request.form['email']):
        flash('Email is not valid!')
        error = True 
        return redirect('/')

    if not error:
        flash("The email address you entered, " + request.form['email'] + ", is a VALID email address! Thank you!")

        query = "INSERT INTO email (email_address, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        
        data = {
                 'email': request.form['email'],
               }
        
        mysql.query_db(query, data)    

    return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM email"
    email = mysql.query_db(query)
    return render_template('index.html', all_email=email)



app.run(debug=True)