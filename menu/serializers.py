from rest_framework import serializers
from .models import Item, Order, Customer

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'
		
class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'