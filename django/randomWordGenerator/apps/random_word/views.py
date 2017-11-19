# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	if 'number' not in request.session:
		request.session['number'] = 1
		request.session['random_string'] = get_random_string(length=14).upper()
		return render(request, 'random_word/index.html')
	else: 
		request.session['number'] += 1
		request.session['random_string'] = get_random_string(length=14).upper()
		return render(request, 'random_word/index.html')	

def reset(request):
	request.session['number'] = 0
	return redirect('/')		

