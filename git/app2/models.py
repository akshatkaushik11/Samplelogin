# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
	name=models.CharField(max_length=50,blank=False)
	password=models.CharField(max_length=50,blank=False)
	dob=models.CharField(max_length=50,default='11/11/1997')
	contact=models.CharField(max_length=50)
	fb=models.CharField(max_length=50,blank=False)
	git=models.CharField(max_length=50,blank=False)
	red=models.CharField(max_length=50,blank=False)
	username=models.CharField(max_length=50,blank=False)

	def __str__(self):
		return self.name


