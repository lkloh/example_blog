# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from django import db
from django.test import TestCase


from debate.decorators import get_num_queries
from debate.models import User, Post, Comment


# Create your tests here.

class UserModelTests(TestCase):

	@get_num_queries
	def test_user_name_empty_string(self):
		empty_name_user = User("")
		self.assertEquals(empty_name_user.name, "")


class PostModelTest(TestCase):

	def setUp(self):
		alice = User.objects.create(name="Alice")
		bob = User.objects.create(name="Bob")
		charlie = User.objects.create(name="Charlie")
		dave = User.objects.create(name="Dave")

		alice_post = Post.objects.create(author=alice, text="I am in wonderland")
		bob_post = Post.objects.create(author=bob, text="My real name is Robert")
		charlie_post = Post.objects.create(author=charlie, text="Born during the Great Depression.")
		dave_post = Post.objects.create(author=dave, text="Many have my name")

		Comment.objects.create(text="Wish I was", post=alice_post, commenter=bob)
		Comment.objects.create(text="Wish I was too", post=alice_post, commenter=charlie)
		Comment.objects.create(text="Wish I was", post=alice_post, commenter=dave)
		Comment.objects.create(text="Mine is Charles", post=bob_post, commenter=charlie)
		Comment.objects.create(text="Lucky I'm not then.", post=charlie_post, commenter=dave)
		Comment.objects.create(text="Born during the renaissance.", post=charlie_post, commenter=alice)

	#@get_num_queries
	def test_post_with_comments(self):
		conn = db.reset_queries()
		for post in Post.objects.all():
			for comment in post.comment_set.filter(hidden=False).all():
				print comment
		print sum(len(conn.queries) for conn in db.connections.all())




