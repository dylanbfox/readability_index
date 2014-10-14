from django.db import models

class Entry(models.Model):

	title = models.CharField(max_length=1024)
	summary = models.TextField()
	author = models.CharField(max_length=1024)
	link = models.CharField(max_length=1024)
	e_id = models.CharField(max_length=1024)
	score = models.IntegerField()

