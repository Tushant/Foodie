from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import AddRestaurantForm

def home(request):
	return render(request, 'restaurant/homepage.html')


# @require_POST
def add_restaurant(request):
	form = AddRestaurantForm(request.POST)
	print('form',form)
	if form.is_valid():
		form.save()
		return redirect('/')
	form = AddRestaurantForm()
	return render(request, 'restaurant/add_restaurant.html',{'form':form})