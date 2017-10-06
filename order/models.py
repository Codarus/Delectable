from django.db import models

# Create your models here.

class Order(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=50, default='###-###-####')
	
	#Admin
	status = models.CharField(max_length=10, default='open')
	
	def __str__(self):
		return self.name
	
	
	