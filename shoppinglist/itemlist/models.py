from django.db import models

class Item(models.Model):
	name = models.CharField(max_length=300)
	description = models.CharField(max_length=300)
	quantity = models.DecimalField(max_digits=50, decimal_places=2)

	def __str__(self):
		return self.name

	def get_absolute_url(self):		
		return f"/item/{self.pk}"
