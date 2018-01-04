# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.exceptions import ObjectDoesNotExist

import re
import bcrypt



# Create your models here.
class UserManager(models.Manager):
	def validate(self, data):
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
		errors = []
		email = data['email']
		if len(data['fname']) == 0:
			errors.append("Please include first name")
		if len(data['fname']) < 2 or not data['fname'].isalpha():
			errors.append("First name must be more than 2 characters and letters only")
		if len(data['lname']) == 0:
			errors.append("Please include last name")
		if len(data['lname']) < 2 or not data['lname'].isalpha():
			errors.append("Last name must be more than 2 characters and letters only")		
		if len(data['email']) == 0:
			errors.append("Please include email")	
		if not len(data['email']) == 0 and not EMAIL_REGEX.match(data['email']):
			errors.append("Please enter a valid email address")		
		if len(data['pword']) == 0:
			errors.append("Please include a password")						
		if len(data['pword']) < 8:
			errors.append("Password must be no fewer than 8 characters")
		if data['pword'] != data['pwconfirm']:
			errors.append("Password must match Confirm Password")	
		if len(errors) > 0:
			return False, errors	
		else: 		
			try:
				if User.objects.get(email=email):
					errors.append("Email address already registered with other user")
					return False, errors		
			except ObjectDoesNotExist:
				return True,	

	def create_user(self, data):
		hash1 = bcrypt.hashpw(data['pword'].encode(), bcrypt.gensalt())
		new_user = User.objects.create(
			first_name=data['fname'], 
			last_name=data['lname'], 
			email=data['email'], 
			pw_hash=hash1)
		return new_user

	def login_user(self, logData):
		errors = []
		email = logData['logemail']
		pword = logData['logpw']
		try:
			user = User.objects.get(email=email)
			if bcrypt.checkpw(pword.encode(), user.pw_hash.encode()):
				return True, 
			else: 
				errors.append("Email address and Password do not match")
				return False, errors 	
					
		except ObjectDoesNotExist:
				errors.append("Email address does not match any user on file")	
				return False, errors	


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)	
	email = models.CharField(max_length=255)
	pw_hash = models.CharField(max_length=255) 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()