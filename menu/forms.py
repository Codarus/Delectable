from django import forms
from menu.models import Order, Customer

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('name', 'name', 'email', 'phone','delivery_date','shipping_info','billing_info',
		'notes','ordered_by','total','surcharge')
		
class CustForm(forms.ModelForm):
	class Meta:
		model =  Customer
		fields = '__all__'
		
class UpdateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('status',)
		
class SearchForm(forms.ModelForm):
	name = forms.CharField(required=False)
	email = forms.EmailField(required=False)
	phone = forms.CharField(required=False)

	class Meta:
		model = Order
		fields = ('name','email','phone')
		
class SearchDateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('delivery_date',)
		
class SeeProfitForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('delivery_date',)