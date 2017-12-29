# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import Course, CourseManager

# Create your views here.
def index(request):
	if request.method == "POST":
		result = Course.objects.validate(request.POST)
		if result[0]:
			Course.objects.create(course_name=request.POST['course_name'], desc=request.POST['desc'])
			messages.success(request, "Thank you for creating a course!")
			return redirect('/')
 		else:
			errors = result[1]	
			for error in errors:
				messages.error(request, error)
			return redirect('/')
 	else:
 		context = {
 		"courses": Course.objects.all()
 		}
 		return render (request, "courses1/index.html", context)

def show(request, course_id):
	context = {
	"course": Course.objects.get(id=course_id)
	}
 	return render(request, 'courses1/show.html', context)

def destroy(request, course_id):
	Course.objects.filter(id=course_id).delete()
 	return redirect('/')
 	 	 	 		