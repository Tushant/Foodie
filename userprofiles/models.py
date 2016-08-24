from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.dispatch import receiver

from django.db import models

from restaurants.models import Restaurant
from orders.models import OrderMenu

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	slug = models.SlugField(unique=True,blank=True,null=True)
	restaurant = models.ManyToManyField(Restaurant, blank=True)
	order_history = models.ManyToManyField(OrderMenu, blank=True)
	# favorites = models.ManyToManyField(Restaurant)
	is_owner = models.BooleanField(default=False)

	class Meta:
		def __str__(self):
			return self.user.username

	@property
	def total_purchase(self):
		total_purchase = 0
		# user_order = UserProfile.objects.prefetch_related('order_history').get(slug=self.slug)
		userprofile = UserProfile.objects.get(slug=self.slug)
		user_order = userprofile.order_history.all()
		for usr in user_order:
			total_purchase += usr.get_cost()
		return total_purchase
	

def create_slug(instance, new_slug=None):
	print('instance',instance.user)
	slug = slugify(instance.user.username)
	if new_slug is not None:
		slug = new_slug
	qs = UserProfile.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

from django.db.models.signals import pre_save
pre_save.connect(pre_save_post_receiver, sender=UserProfile)

	# def get_absolute_url(self):
	# 	return reverse('userprofiles:profile', kwargs={'slug':self.slug, 'id':self.id}) #args=[self.id, self.slug]


def create_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)
		print('instance',instance, 'profile',profile, 'created',created)

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)


# userprofile = UserProfile.objects.get(user=User.objects.get(username=request.user))
# userprofile.restaurant.add(Restaurant.objects.get(owner=request.user))