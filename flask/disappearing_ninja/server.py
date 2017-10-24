from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ninja')
def all_ninjas():	
	return render_template("ninja.html", ninja="")

@app.route('/ninja/<color>')
def show_ninja(color):	
	turtle = {'purple': 'donatello', 'blue': 'leonardo', 'orange': 'michelangelo', 'red': 'raphael'}
	ninja = turtle.get(color, 'notapril')

	return render_template("ninja.html", ninja=ninja)

app.run(debug=True)	