# from multiselectfield import MultiSelectField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.db import models


class Choice(models.Model):
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

	features = models.CharField(max_length=2, choices=FEATURE_CHOICES, default=DINNER)
	timings = models.CharField(max_length=2, choices=TIMING_CHOICES, default=MONDAY)

	def __str__(self):
		return self.features


class Restaurant(models.Model):
	OPEN = 1
	CLOSED = 2

	OPENING_STATUS = (
		(OPEN, 'open'),
		(CLOSED, 'closed'),
		)

	# STARS = (
	# 		(1, 'one'),
	# 		(2, 'two'),
	# 		(3, 'three'),
	# 		(4, 'four'),
	# 		(5, 'five'),
	# 	)

	owner = models.ForeignKey(User)
	name = models.CharField(max_length=150, db_index=True)
	slug = models.SlugField(max_length=150, db_index=True)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	phone_number = models.PositiveIntegerField()
	owner_email = models.EmailField()
	opening_status = models.IntegerField(choices=OPENING_STATUS, default=OPEN)
	website = models.URLField(max_length=300)
	features = models.ManyToManyField(Choice, related_name="restaurants_features")
	timings = models.ManyToManyField(Choice, related_name="restaurants_timings")
	opening_from = models.TimeField()
	opening_to = models.TimeField()
	facebook_page = models.URLField(max_length=200)
	twitter_handle = models.CharField(max_length=15, blank=True, null=True)
	other_details = models.TextField()
	# votes = models.IntegerField(choices=STARS, default=5)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ('name',)
		index_together = (('id','slug'),)


	def __str__(self):
		return self.restaurant_name

	# def get_absolute_url(self):
	# 	return reverse('restaurant:restaurant_detail', args=[self.id, self.slug])


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

	# def get_absolute_url(self):
	# 	return reverse('restaurant:menu_detail', args=[self.id, self.slug])