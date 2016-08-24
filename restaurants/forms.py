from django import forms 

from .models import Restaurant

class AddRestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		exclude = ('owner','slug','available','lat','lang','image','created','updated',)


class FavoriteForm(forms.Form):
	type = forms.CharField(max_length=10)
	id = forms.IntegerField()