from datetime import datetime

# from multiselectfield import MultiSelectField
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from geopy.geocoders import Nominatim
from django.db import models

from review.models import Review

class FeatureChoice(models.Model):
	BREAKFAST = 'BR'
	LAUNCH = 'LA'
	DINNER = 'DI'
	DELIVERY = 'DE'
	CAFE = 'CA'
	LUXURY = 'LU'
	NIGHT = 'NI'

	FEATURE_CHOICES = (
		(BREAKFAST, 'Breakfast'),
		(LAUNCH, 'Launch'),
		(DINNER, 'Dinner'),
		(DELIVERY, 'Delivery'),
		(CAFE, 'Cafe'),
		(LUXURY, 'Luxury Dining'),
		(NIGHT, 'Night Life'),
		)



	features = models.CharField(max_length=2, choices=FEATURE_CHOICES, default=DINNER)

	def __str__(self):
		return self.features

class TimingChoice(models.Model):
	MONDAY = 'MO'
	TUESDAY = 'TU'
	WEDNESDAY = 'WE'
	THURSDAY = 'TH'
	FRIDAY = 'FR'
	SATURDAY = 'SA'
	SUNDAY = 'SU'

	TIMING_CHOICES = (
		(MONDAY, 'Monday'),
		(TUESDAY, 'Tuesday'),
		(WEDNESDAY, 'Wednesday'),
		(THURSDAY, 'Thursday'),
		(FRIDAY, 'Friday'),
		(SATURDAY, 'Saturday'),
		(SUNDAY, 'Sunday'),
		)
	timings = models.CharField(max_length=2, choices=TIMING_CHOICES, default=MONDAY)

	def __str__(self):
		return self.timings

class Favorite(models.Model):
	restaurant = models.ForeignKey('Restaurant')
	ip = models.CharField(max_length=19)
	user_agent = models.TextField(blank=True, null=True)
	mark_favorite = models.CharField(max_length=20)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('restaurant','ip',)

	@classmethod
	def create_favorite_for_count(cls, request, restaurant):
		print('cls',cls)
		ip = request.META.get('HTTP_X_FORWARDED_FOR')
		ip = request.META.get('REMOTE_ADDR') if ip is None else ip
		user_agent = request.META.get('HTTP_USER_AGENT')
		mark_favorite, created = cls.objects.get_or_create(restaurant=restaurant, ip=ip, user_agent=user_agent)
		return mark_favorite

class Restaurant(models.Model):
	OPEN = 1
	CLOSED = 2

	OPENING_STATUS = (
		(OPEN, 'open'),
		(CLOSED, 'closed'),
		)
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=150, db_index=True)
	slug = models.SlugField(max_length=150, db_index=True)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	lat = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
	lag = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
	phone_number = models.PositiveIntegerField()
	owner_email = models.EmailField()
	opening_status = models.IntegerField(choices=OPENING_STATUS, default=OPEN)
	website = models.URLField(max_length=300, blank=True, null=True)
	features = models.ManyToManyField(FeatureChoice, related_name='restaurants_features')
	timings = models.ManyToManyField(TimingChoice, related_name='restaurants_timings')
	image = models.ImageField(upload_to='upload/products/%Y/%m/%d', blank=True)
	facebook_page = models.URLField(max_length=200,blank=True, null=True)
	twitter_handle = models.CharField(max_length=15, blank=True, null=True)
	other_details = models.TextField()
	is_parking = models.BooleanField(default=False)
	is_wifi = models.BooleanField(default=False)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	@property
	def count_favorite(self):
		return Favorite.objects.filter(mark_favorite='favorite', restaurant=self).count()

	@property
	def review(self):
		instance = self
		print('instance from model is ',instance)
		qs = Review.objects.filter_by_instance(self)
		return qs

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance)
		print('content_type is',content_type)
		return content_type
	

	class Meta:
		ordering = ('name',)
		unique_together = (('id','name'),)
		index_together = (('id','slug'),)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('restaurants:restaurant_detail', args=[self.slug])

def create_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug
	qs = Restaurant.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

from django.db.models.signals import pre_save
pre_save.connect(pre_save_post_receiver, sender=Restaurant)


class OperatingTime(models.Model):
	MONDAY = 1
	TUESDAY = 2
	WEDNESDAY = 3
	THURSDAY = 4
	FRIDAY = 5
	SATURDAY = 6
	SUNDAY = 7

	DAY_IN_A_WEEK = (
		(MONDAY, 'Monday'),
		(TUESDAY, 'Tuesday'),
		(WEDNESDAY, 'Wednesday'),
		(THURSDAY, 'Thursday'),
		(FRIDAY, 'Friday'),
		(SATURDAY, 'Saturday'),
		(SUNDAY, 'Sunday'),
		)
	# HOURS = [(i, i) for i in range(1, 25)]
	restaurant = models.ForeignKey(Restaurant,related_name="operating_time")
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	day_of_week = models.IntegerField(choices=DAY_IN_A_WEEK)

	@property
	def open_or_closed(self):
		operating_time = OperatingTime.objects.all()
		opening_time = operating_time.opening_time
		closing_time = operating_time.closing_time
		current_time =  datetime.now().time()
		weekday = operating_time.day_of_week
		if opening_time < current_time < closing_time:
			open_or_closed = True
		else:
			open_or_closed = False 
		return open_or_closed
	

	def __str__(self):
		return '{} ---- {}'.format(self.opening_time, self.closing_time)


class MenuCategory(models.Model):
	name = models.CharField(max_length=120,db_index=True) #veg, non-veg
	slug = models.SlugField(max_length=120,db_index=True)

	class Meta:
		ordering=('name', )
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name



class Menu(models.Model):
	STARS = (
		(1, 'one'),
		(2, 'two'),
		(3, 'three'),
		(4, 'four'),
		(5, 'five'),
	)
	menu_category = models.ForeignKey(MenuCategory, related_name="menu")
	restaurant = models.ForeignKey(Restaurant)
	name = models.CharField(max_length=120,db_index=True)
	slug = models.SlugField(max_length=120,db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	stock = models.PositiveIntegerField()
	vote = models.SmallIntegerField(choices=STARS, default=5)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	class Meta:
		ordering=('name', )
		index_together = (('id', 'slug'), )

	def __str__(self):
		return self.name

def create_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug
	qs = Menu.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

from django.db.models.signals import pre_save
pre_save.connect(pre_save_post_receiver, sender=Menu)

	# def get_absolute_url(self):
	# 	return reverse('restaurant:menu_detail', args=[self.id, self.slug])



# def save_lat_and_lang_from_address(sender, instance, created, *args, **kwargs):
# 	print('instance is', instance.address)
# 	geolocator = Nominatim()
# 	location=geolocator.geocode(str(instance.address))
# 	print('location is',location)
# 	# instance.lat = location.latitude
# 	# instance.lang = location.longitude
# 	instance.save()
# post_save.connect(save_lat_and_lang_from_address, sender=Restaurant)


# operating_time = OperatingTime.objects.all()
# print('operating time',operating_time)
# for operating_time in operating_time:
# 	opening = operating_time.opening_time
# 	closing = operating_time.closing_time
# 	print('opening',opening)
# current_time = datetime.now()
# current_time = current_time.time()
# if current_time < closing or opening< current_time:
# 	print('opening')
# else:
# 	print('closed')
	# TODO to find out if restaurant is open or not first find the opening time and then find current time and ofcourse closing time
	# then calculate the difference between current time and opening time. if < closing_time or greater than opening_time available