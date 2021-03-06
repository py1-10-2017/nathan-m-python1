# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
class Comment(models.Model):
	comment = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	blog = models.ForeignKey(Blog, related_name = "comments")
class Admin(models.Model):
	comment = models.CharField(max_length = 255)
	comment = models.CharField(max_length = 255)
	comment = models.CharField(max_length = 255)
	blogs = models.ManyToManyField(Blog, related_name = "admins")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)		