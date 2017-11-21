# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import strftime
from datetime import datetime

def index(request):
	return render(request, 'session_words/index.html')		

def add_word(request):
    new_word = {}
    for key, value in request.POST.iteritems():
    	print "val or value" + '*'* 50
        if key != "csrfmiddlewaretoken" and key != "font_size":
            new_word[key] = value
        if "font_size" not in request.POST:
        	new_word['font_size'] = ""
        else:
            new_word['font_size'] = "big"
    new_word['time'] = datetime.now().strftime("%I:%M %p, %B %d, %Y")
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    temp = request.session['words']
    temp.append(new_word)
    request.session['words'] = temp

    for key, val in request.session.__dict__.iteritems():
        print key, val
        print "check" + '*'* 50
    print "past created at", new_word
    print "this also" + '*'* 50

    return redirect('/')

def reset(request):
	for key in request.session.keys():
		del request.session[key]
	return redirect('/')
