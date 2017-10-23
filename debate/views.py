# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from debate.models import User, Post, Comment

# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def users(request):
	users = [user for user in User.objects.all()]
	return render(request, 'debate/users.html', {'users': users})

def posts(request):
	posts = [post for post in Post.objects.all()]
	return render(request, 'debate/posts.html', {'posts': posts})
