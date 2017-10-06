from django.shortcuts import render
from .forms import OrderForm

from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics

"""
def index(request):
	form = OrderForm(request.POST or None)
	context = {"form":form}
	template = "order/home.html"
	return render(request, template, context)
"""
#form handling
def index(request):
	form = OrderForm(request.POST or None)
	if form.is_valid():
		new_order = form.save(commit=False)
		new_order.save()
		print(new_order)
		
	context = {"form":form}
	template = "order/home.html"
	return render(request, template, context)
	
class OrderList(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
