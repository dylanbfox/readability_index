from django.db import models

class Entry(models.Model):

	class Meta:
		ordering = ['-created']

	title = models.CharField(max_length=1024)
	summary = models.TextField()
	link = models.CharField(max_length=1024)
	e_id = models.CharField(max_length=1024)
	raw_score = models.DecimalField(decimal_places=2, max_digits=4)
	rounded_score = models.IntegerField()
	wps = models.DecimalField(decimal_places=2, max_digits=4)
	lpw = models.DecimalField(decimal_places=2, max_digits=4)
	ignore = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

