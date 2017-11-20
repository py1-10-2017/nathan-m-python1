# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect


def index(request):
  	return render (request, 'surveys/index.html')

def process(request):  
	if request.method == 'POST':		
		request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
	return redirect('/result')

def result(request):
	return render(request, 'surveys/result.html')	

