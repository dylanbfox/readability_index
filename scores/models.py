from django.db import models

class Entry(models.Model):

	title = models.CharField(max_length=1024)
	summary = models.TextField()
	author = models.CharField(max_length=1024)
	link = models.CharField(max_length=1024)
	e_id = models.CharField(max_length=1024)
	raw_score = models.DecimalField(decimal_places=2, max_digits=4)
	rounded_score = models.IntegerField()
	wps = models.DecimalField(decimal_places=2, max_digits=4)
	lpw = models.DecimalField(decimal_places=2, max_digits=4)

