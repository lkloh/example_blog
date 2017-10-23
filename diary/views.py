# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from diary.models import User, Post, Comment

# Create your views here.

def user_list(request):
	return render(request, 'diary/user_list.html')


