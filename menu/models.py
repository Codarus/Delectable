from django.db import models
from django.utils.timezone import localtime, now

# Create your models here.

class Item(models.Model):
	name = models.CharField(max_length=50)
	price_per_person = models.CharField(max_length=5)
	minimum_order = models.CharField(max_length=5)
	categories = models.CharField(max_length=50, blank=True)
	
	create_date = models.DateField(auto_now_add=True, blank=True, null=True)
	last_modified_date = models.DateField(auto_now=True, blank=True, null=True)
	
	def __str__(self):
		return self.name
		
class Order(models.Model):

	order_date = models.DateField(default=localtime(now()).date())
	delivery_date = models.DateField(default=localtime(now()).date())
	status = models.CharField(max_length=10, default='open')
	ordered_by = models.CharField(max_length=50, null=True)
	
	#user input
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=50)
	shipping_info = models.CharField(max_length=50, null=True)
	billing_info = models.CharField(max_length=50, null=True)
	notes = models.CharField(max_length=150)
	total = models.DecimalField(default=0, max_digits=5, decimal_places=2)
	surcharge = models.DecimalField(default=0, max_digits=5,decimal_places=2)
	
	def __str__(self):
		return self.name
		
class Customer(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name