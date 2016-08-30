import json
from datetime import datetime, time

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.http import require_POST
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Count 

from .models import Restaurant, OperatingTime, Favorite
from .forms import AddRestaurantForm, FavoriteForm
from review.forms import ReviewForm
from review.models import Review
from restaurants.utils import nearby_restaurants
from restaurants.utils import CustomEncoder


def base(request):
	restaurant = Restaurant.objects.all().annotate(mark_favorite=Count('favorite__restaurant')).order_by('mark_favorite')
	return render(request, 'restaurant/base.html', {'restaurant':restaurant})

def homepage(request):
	restaurant = Restaurant.objects.all().annotate(mark_favorite=Count('favorite__restaurant')).order_by('mark_favorite')
	operating_time = OperatingTime.objects.all()
	# review = Review.objects.all()
	print('restaurant',restaurant)
	return render(request, 'restaurant/homepage.html', {'restaurant':restaurant})


def restaurant_detail(request, restaurant_slug):
	restaurant_instance = get_object_or_404(Restaurant, slug=restaurant_slug)
	# content_type = ContentType.objects.get_for_model(Restaurant)
	# obj_id = restaurant.id # Restaurant.objects.get(id=restaurant.id)
	# reviews = Review.objects.filter_by_instance(instance)
	initial_data = {
		'content_type':restaurant_instance.get_content_type, # no need to give () because its a parenthesis
		'object_id':restaurant_instance.id
	}
	form = ReviewForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		print('review form',form.cleaned_data)
		c_type = form.cleaned_data.get('content_type')
		print('c_type',c_type)
		content_type = ContentType.objects.get(model=c_type)
		print('content_type form',content_type)
		object_id = form.cleaned_data.get('object_id')
		review = form.cleaned_data.get('review')
		parent_obj = None
		try:
			parent_id = int(request.POST.get('parent_id')) # <input type="hidden" name="parent_id" />
			print('parent_id',parent_id)
		except:
			parent_id = None
		if parent_id:
			parent_qs = Review.objects.filter(id=parent_id)
			print('parent_qs',parent_qs)
			if parent_qs.exists():
				parent_obj = parent_qs.first()
				print('parent_obj',parent_obj)
		new_review, created = Review.objects.get_or_create(
								reviewer = request.user,
								content_type = content_type,
								object_id = object_id,
								review = review,
								parent = parent_obj
								)
		return redirect(new_review.content_object.get_absolute_url())
	reviews = restaurant_instance.review
	return render(request, 
				'restaurant/restaurant_detail.html', 
				{'restaurant_instance':restaurant_instance, 
				'reviews':reviews,
				'review_form':form
				})

class FavoriteView(View):
	def post(self, request, *args, **kwargs):
		form = FavoriteForm(request.POST)
		status = {}
		if form.is_valid():
			restaurant = get_object_or_404(Restaurant, pk=form.cleaned_data['id'])
			print(restaurant)
			favorite = Favorite.create_favorite_for_count(request, restaurant)
			favorite.mark_favorite = form.cleaned_data['type']
			favorite.save()
			status['message']='Thank you for giving me your heart';
			status['status_code']=200;
			messages.success(request, 'Thanks for giving me your heart!')
		else:
			status['message']='Error';
			status['status_code']=400;
			messages.warning(request, 'something is wrong')
		status['favorite_count']= restaurant.count_favorite
		return HttpResponse(json.dumps(status), content_type='text/json')


# @require_POST
def add_restaurant(request):
	form = AddRestaurantForm(request.POST)
	print('form',form)
	if form.is_valid():
		form.save()
		return redirect('/')
	form = AddRestaurantForm()
	return render(request, 'restaurant/add_restaurant.html',{'form':form})

def search_restaurant(request):
	latitude = request.GET.get('latitude', None)
	longitude = request.GET.get('longitude', None)
	if latitude and longitude:
		restaurants = nearby_restaurants(latitude, longitude)
		return HttpResponse(json.dumps(restaurants, cls=CustomEncoder))
	else:
		return HttpResponse(json.dumps({'status':False}))
