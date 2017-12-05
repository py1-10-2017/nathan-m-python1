# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

import random
from datetime import datetime
# Create your views here.

def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
		request.session['activities'] = []
	return render(request, "ninjaGold/index.html")

def process_money(request):
	time_of_click = datetime.now().strftime("%Y-%m-%d %H:%M")
	location = request.POST['loc']
	if location == "farm":
		gold = random.randint(10, 20)
		request.session['activities'].append({'activity':'Earned {} golds from the farm! ({})'.format(gold, time_of_click), 'class':'gain'})
	elif location == "cave":
		gold = random.randint(5, 10)
		request.session['activities'].append({'activity':'Earned {} golds from the cave! ({})'.format(gold, time_of_click), 'class':'gain'})
	elif location == "house":
		gold = random.randint(2, 5)
		request.session['activities'].append({'activity':'Earned {} golds from the house! ({})'.format(gold, time_of_click), 'class':'gain'})
	elif location == "casino":
		gold = random.randint(-50, 50)
		if gold > 0:
			request.session['activities'].append({'activity':'Entered a casino and won {} golds! ({})'.format(gold, time_of_click), 'class':'gain'})	
		else:
			request.session['activities'].append({'activity':'Entered a casino and lost {} golds! ({})'.format(gold, time_of_click), 'class':'lose'})

	request.session['gold'] += gold
	return redirect('/')

def reset(request):
	request.session.pop('gold')
	request.session.pop('activities')
	return redirect('/')

