# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import Comment

# Create your views here.
def index(request):
	return render(request, 'ajaxPost/index.html')

def create(request):
	if request.method == "POST":
		Comment.objects.create(comment=request.POST['comment'])
		return render(request, 'ajaxPost/all.html', { "comments": Comment.objects.order_by("-id") })
	else:
		return redirect('/')
	