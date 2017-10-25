# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from django.test import TestCase


from debate.decorators import get_num_queries
from debate.models import User, Post, Comment


# Create your tests here.

class UserModelTests(TestCase):

	@get_num_queries
	def test_user_name_empty_string(self):
		empty_name_user = User("")
		self.assertEquals(empty_name_user.name, "")

