from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Avg

from django.db import models

class ReviewManager(models.Manager):
	def all(self):
		qs = super(ReviewManager, self).filter(parent=None)
		return qs

	def filter_by_instance(self, instance):
		print('instance is',instance) # Kathmandu Fast Food Center
		# content_type = ContentType.objects.get_for_model(Restaurant)
		content_type = ContentType.objects.get_for_model(instance.__class__)
		obj_id = instance.id # Restaurant.objects.get(id=restaurant.id)
		qs = super(ReviewManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
		# Review.objects is replaced by super(ReviewManager,self)
		return qs



class Review(models.Model):
	reviewer = models.ForeignKey(User) #user
	# slug = models.SlugField(max_length=150,blank=True)
	# restaurant = models.ForeignKey(Restaurant) #Post

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # these 3 items are gonna takes place of restaurant foriegn key
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	parent = models.ForeignKey("self", null=True, blank=True, related_name="parent_review")
	review = models.TextField() #content
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	objects = ReviewManager() # this gives to replace Review.objects in above code 

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return '{} - {}'.format(self.reviewer,self.review[:30]) 

	def children(self): # replies
		return Review.objects.filter(parent=self)

	@property	
	def is_parent(self):
		if self.parent is not None: # if there is a parent then inside of parent field then its not a parent
			return False 
		return True 

class Rate(models.Model):
	STARS = (
			(1, 'one'),
			(2, 'two'),
			(3, 'three'),
			(4, 'four'),
			(5, 'five'),
		)
	rater = models.ForeignKey(User)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
	object_id = models.PositiveIntegerField(null=True)
	content_object = GenericForeignKey('content_type', 'object_id')
	rate = models.SmallIntegerField(choices=STARS, default=5)

	# @property
	# def average_rating(self):
	# 	restaurant = Restaurant.objects.get(pk=self.pk)
	# 	stars_average = restaurant.review_set.aggregate(Avg('vote')).values()
	# 	print('stars_average',stars_average)
	# 	return stars_average

	def __str__(self):
		return '{} {}'.format(self.rater.username, self.rate)