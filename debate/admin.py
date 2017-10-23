# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from debate.models import User, Post, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)

