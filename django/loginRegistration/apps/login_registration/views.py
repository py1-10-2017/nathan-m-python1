# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import User, UserManager

# Create your views here.
def index(request):
	try:
		if request.session['user']:
			return redirect('/show')
			
	except (KeyError):
		return render(request, 'login_registration/index.html')			

def create(request):
	if request.method == 'POST':
		result = User.objects.validate(request.POST)
		if result[0]:
			new_user = User.objects.create_user(request.POST)
			log_user = User.objects.get(id=new_user.id)
			request.session['user'] = log_user.id
			return redirect('/show')
		else: 
			errors = result[1]
			for error in errors:
				messages.error(request, error)	
			return redirect('/')	
	else:
		return redirect('/')

def login(request):
	if request.method == 'POST':
		result = User.objects.login_user(request.POST)
		if result[0]:
			email = request.POST['logemail']
			log_user = User.objects.get(email=email)
			request.session['user'] = log_user.id
			return redirect('/show')
		else: 
			errors = result[1]
			for error in errors:
				messages.error(request, error)	
			return redirect('/')				


def show(request):
	context = {
	'user': User.objects.get(id=request.session['user'])
	}
	return render(request, 'login_registration/success.html', context)

def destroy(request):
	request.session.pop('user')
	return redirect('/')