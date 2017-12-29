# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User, UserManager

# Create your views here.
def index(request):
	if request.method == "POST":
		result = User.objects.validate(request.POST)
		if result[0]:
			User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'])
			messages.success(request, "Thank you for creating a user")
		# User.objects.validate(request.POST)
 			return redirect('/')
 		else:
			errors = result[1]	
			for error in errors:
				messages.error(request, error)
			return redirect('/')
 	else:
 		context = {
 		"users": User.objects.all()
 		}
 		return render (request, "users/index.html", context)

def new(request):	
 	return render(request, 'users/new.html')

def edit(request, user_id):
	context = {
	"user": User.objects.get(id=user_id)
	}	
 	return render(request, 'users/edit.html', context)

def show(request, user_id):
	context = {
	"user": User.objects.get(id=user_id)
	}
 	return render(request, 'users/show.html', context)

def destroy(request, user_id):
	User.objects.filter(id=user_id).delete()
 	return redirect('/')

def update(request, user_id):
	u = User.objects.get(id=user_id)
	u.first_name = request.POST['fname']
	u.last_name = request.POST['lname']
	u.email = request.POST['email']
	u.save()
 	return redirect('/') 