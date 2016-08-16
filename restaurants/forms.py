from django.forms import ModelForm 

from .models import Restaurant

class AddRestaurantForm(ModelForm):
	class Meta:
		model = Restaurant
		exclude = ('owner','slug','available','created','updated',)
