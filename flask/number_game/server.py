from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'somewhatSecret'

@app.route('/')
def index():
	if 'correct_num' not in session:
		session['correct_num'] = random.randint(1, 101)
  	return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
	guess = int(request.form['number'])
	correct_num = int(session['correct_num'])
	if guess > correct_num:
		session['message'] = "too_high"
	elif guess < correct_num:
		session['message'] = "too_low"
	else:
		session['message'] = "correct"
	return render_template("index.html")

@app.route('/reset')
def reset():
	session.pop('correct_num')
	session.pop('message')
	return redirect('/')

app.run(debug=True)