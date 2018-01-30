# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)