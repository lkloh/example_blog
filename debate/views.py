# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from debate.models import User

# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def user_list(request):
	user_list = [user for user in User.objects.all()]
	#return HttpResponse('User')
	return render(request, 'debate/user_list.html', {'user_list': user_list})
