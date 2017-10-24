from flask import Flask, render_template, request, flash, redirect, session
app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')

def index():
  return render_template("index.html")

@app.route('/check', methods=['POST'])

def check():
	if len(request.form['name']) == 0:
		flash('Name must not be blank')

	if len(request.form['comment']) > 120:
		flash('Comment must not be over 120 characters')

	if len(request.form['name']) == 0 or len(request.form['comment']) > 120:	
		return redirect('/')	

	session['all_info']	= request.form
	return redirect('/result')

@app.route('/result')

def result():
	return render_template('result.html', result=session['all_info'])

app.run(debug=True)