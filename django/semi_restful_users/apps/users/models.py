# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def validate(self,data):
		errors = []
		if len(data['fname']) == 0:
			errors.append("Please include first name")
		if len(data['lname']) == 0:
			errors.append("Please include last name")			
		if len(data['email']) == 0:
			errors.append("Please include email")	
		if len(errors) == 0:
			return True, 
		if len(errors) > 0:
			return False, errors


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, default=" ")	
	email= models.CharField(max_length=255) 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()