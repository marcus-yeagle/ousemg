from django.db import models

class Member(models.Model):
	def __str__(self):
		return self.first_name

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	major = models.CharField(max_length=50)
	year = models.CharField(max_length=50)
	group_status = (
		('Board', 'Executive Board'),
		('Head', 'Head Analyst'),
		('Analyst', 'Analyst'),
	)
	linkedin_url = models.CharField(max_length=50)





