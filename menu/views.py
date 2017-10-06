from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import *
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.timezone import localtime, now
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

from menu.models import Item, Order, Customer
from menu.forms import OrderForm, CustForm, UpdateForm, SearchForm, SearchDateForm, SeeProfitForm
from .serializers import ItemSerializer, OrderSerializer, CustomerSerializer
from rest_framework import generics

def CreateOrder(request):
	if request.method == 'POST':
		form = OrderForm(request.POST or None, prefix = 'order')
		cform = CustForm(request.POST or None, prefix = 'cust')
		if form.is_valid() or cform.is_valid():
			new_order = form.save(commit=False)
			cnew_order = cform.save(commit=False)
			new_order.save()
			cnew_order.save()
			print(new_order)
			print(cnew_order)
			
		bread = Item.objects.get(name='bread basket')
		fish = Item.objects.get(name='fish')
		rice = Item.objects.get(name='white rice w/ vegetables')
		csalad = Item.objects.get(name='ceasar salad')
		tsoup = Item.objects.get(name='tomato soup')
		tvsoup = Item.objects.get(name='tomato-vegetable soup')
		vsoup = Item.objects.get(name='vegetable soup')
		beverage = Item.objects.get(name='beverage')
		surcharge = Item.objects.get(name='surcharge')
			
		context = {"form":form, "cform":cform,'bread':bread,'fish':fish,
		'rice':rice,'csalad':csalad,'tsoup':tsoup,'tvsoup':tvsoup,'vsoup':vsoup,
		'beverage':beverage,'surcharge':surcharge}
		template = "confirmation/"
		return redirect(template, context)
	else:
		form = OrderForm(prefix = 'order')
		cform = CustForm(prefix = 'cust')
	
		bread = Item.objects.get(name='bread basket')
		fish = Item.objects.get(name='fish')
		rice = Item.objects.get(name='white rice w/ vegetables')
		csalad = Item.objects.get(name='ceasar salad')
		tsoup = Item.objects.get(name='tomato soup')
		tvsoup = Item.objects.get(name='tomato-vegetable soup')
		vsoup = Item.objects.get(name='vegetable soup')
		beverage = Item.objects.get(name='beverage')
		surcharge = Item.objects.get(name='surcharge')
		
		context = {"form":form, "cform":cform,'bread':bread,'fish':fish,
		'rice':rice,'csalad':csalad,'tsoup':tsoup,'tvsoup':tvsoup,
		'vsoup':vsoup,'beverage':beverage,'surcharge':surcharge}
		template = "menu/home.html"
		return render(request, template, context)
	
def ViewOrder(request):
	if request.method == 'POST':
		name = request.POST.get('textfield', None)
		try:
			order = Order.objects.all().filter(name__exact=name)
			#do something with user
			
			context = {'order':order}
			template = "menu/vieworder.html"
			
			return render(request, template, context)
		except Order.DoesNotExist:
			return HttpResponse("no such order")  
	else:
		return render(request, 'menu/vieworder.html')
		
def ConfirmOrder(request):
	new = Order.objects.latest('id')
	print(new)
	context = {'new':new,}
	template = 'menu/confirmation.html'
	return render(request, template, context)
	
def SearchOrder(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['name']:
				name = form.cleaned_data['name']
				try:
					order = Order.objects.all().filter(name__exact=name)
				except Order.DoesNotExist:
					return HttpResponse("no such order") 
					
			elif form.cleaned_data['email']:
				email = form.cleaned_data['email']
				try:
					order = Order.objects.all().filter(email__exact=email)
				except Order.DoesNotExist:
					return HttpResponse("no such order") 
					
			elif form.cleaned_data['phone']:
				phone = form.cleaned_data['phone']
				try:
					order = Order.objects.all().filter(phone__exact=phone)
				except Order.DoesNotExist:
					return HttpResponse("no such order")
			else:
				return HttpResponse("no such order")
			
			context = {'form':form,'order':order}
			template = "menu/searchorder.html"
			return render(request, template, context)
					
	else:
		form = SearchForm()
		dform = SearchDateForm()
		context = {'form':form,'dform':dform}
		template = 'menu/searchorder.html'
		
		return render(request, template, context)

def SearchDateOrder(request):
	if request.method == 'POST':
		form = SearchDateForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['delivery_date'] == localtime(now()).date():
				try:
					date = Order.objects.all().filter(delivery_date__exact=localtime(now()).date())
					context = {'form':form,'date':date}
					template = "menu/searchdateorder.html"
					return render(request, template, context)
				except Order.DoesNotExist:
					return HttpResponse("no such order")
			else:
				return HttpResponse("no orders due today")
				
	else:
		form = SearchDateForm()
		context = {'form':form}
		template = 'menu/searchdateorder.html'
		
		return render(request, template, context)
		
def SeeProfitOrder(request):
	month1 = datetime.today() - timedelta(days=30)
	order1 = Order.objects.all().filter(delivery_date__gte=month1).filter(status__exact='closed')
	
	month2 = datetime.today() - relativedelta(months=+2)
	order2 = Order.objects.all().filter(delivery_date__gte=month1).filter(status__exact='closed')
	
	month3 = datetime.today() - relativedelta(months=+3)
	order3 = Order.objects.all().filter(delivery_date__gte=month1).filter(status__exact='closed')
	
	month6 = datetime.today() - relativedelta(months=+6)
	order6 = Order.objects.all().filter(delivery_date__gte=month1).filter(status__exact='closed')
	
	month12 = datetime.today() - relativedelta(months=+12)
	order12 = Order.objects.all().filter(delivery_date__gte=month1).filter(status__exact='closed')
	
	context = {'month1':month1,'month2':month2,'order1':order1,'order2':order2,'order3':order3,
	'order6':order6,'order12':order12,}
	template = 'menu/ledger.html'
	
	return render(request, template, context)
	
class CancelOrder(UpdateView):
	model = Order
	fields = ('status',)
	template_name = 'menu/order_form.html'
	
	def get_success_url(self):
		return reverse('confirm')
		
class UpdateItem(UpdateView):
	model = Item
	fields = ('price_per_person',)
	template_name = 'menu/item_form.html'
	
	def get_success_url(self):
		return reverse('menu')
		
#API
	
class ItemList(generics.ListCreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	
class OrderList(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class CustomerList(generics.ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer