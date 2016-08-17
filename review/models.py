from django.contrib.auth.models import User

from django.db import models

from restaurants.models import Restaurant


class Review(models.Model):
	STARS = (
			(1, 'one'),
			(2, 'two'),
			(3, 'three'),
			(4, 'four'),
			(5, 'five'),
		)
	vote = models.SmallIntegerField(choices=STARS, default=5)
	user = models.ForeignKey(User)
	restaurant = models.ForeignKey(Restaurant)
	review = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.vote 