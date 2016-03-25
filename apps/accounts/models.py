from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User)
	content = models.TextField()
	likes = models.IntegerField()
	class Meta:
		db_table = 'posts'

class Like(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)

	class Meta:
		db_table = 'likes'