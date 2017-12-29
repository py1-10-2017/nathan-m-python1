# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
	def validate(self,data):
		errors = []
		if len(data['course_name']) < 5:
			errors.append("Course name must be more than 5 characters")
		if len(data['desc']) < 15:
			errors.append("Course description must be more than 15 characters")			
		if len(errors) == 0:
			return True, 
		if len(errors) > 0:
			return False, errors


class Course(models.Model):
	course_name = models.CharField(max_length=255)
	desc = models.TextField()	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CourseManager()