from flask import Flask, render_template, redirect, session, request
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'sortOfaSecret'

@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
		session['activities'] = []
	return render_template("index.html", gold=session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
	time_of_click = datetime.now().strftime("%Y-%m-%d %H:%M")
	location = request.form['loc']
	if location == "farm":
		gold = random.randint(10, 20)
		session['activities'].append({'activity':'Earned {} golds from the farm! ({})'.format(gold, time_of_click), 'class':'gain'})
	elif location == "cave":
		gold = random.randint(5, 10)
		session['activities'].append({'activity':'Earned {} golds from the cave! ({})'.format(gold, time_of_click), 'class':'gain'})
	elif location == "house":
		gold = random.randint(2, 5)
		session['activities'].append({'activity':'Earned {} golds from the house! ({})'.format(gold, time_of_click), 'class':'gain'})
	elif location == "casino":
		gold = random.randint(-50, 50)
		if gold > 0:
			session['activities'].append({'activity':'Entered a casino and won {} golds! ({})'.format(gold, time_of_click), 'class':'gain'})	
		else:
			session['activities'].append({'activity':'Entered a casino and lost {} golds! ({})'.format(gold, time_of_click), 'class':'lose'})
	
	session['gold'] += gold
	return redirect('/')

@app.route('/reset')
def reset():
	session.pop('gold')
	session.pop('activities')
	return redirect('/')

app.run(debug=True)