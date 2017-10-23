# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
    	return self.name

class Post(models.Model):
	text = models.CharField(max_length=4000)
	author = models.ForeignKey(User)

	def __str__(self):
		return self.text

class Comment(models.Model):
	text = models.CharField(max_length=400)
	post = models.ForeignKey(Post)
	commenter = models.ForeignKey(User)
 	hidden = models.BooleanField(default=False)

 	def __str__(self):
		return 'Comment: %s, Post: %s, Commenter: %s' % (self.text, str(self.post), str(self.commenter))
