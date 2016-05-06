from django.db import models
from django.core.urlresolvers import reverse


class Member(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	major = models.CharField(max_length=50)
	year = models.CharField(max_length=50)
	group_status = models.CharField(max_length=50)
	linkedin_url = models.CharField(max_length=50)
	pic = models.FileField(null=True, blank=True)

	def __str__(self):
		return self.first_name

	def get_absolute_url(self):
		return reverse('members:detail', kwargs={"id":self.id})

	