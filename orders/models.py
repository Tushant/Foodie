from django.db import models

from restaurants.models import Menu, Restaurant

class Order(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	address = models.CharField(max_length=250)
	postal_code = models.CharField(max_length=20, blank=True, null=True)
	city = models.CharField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

    
    
class OrderMenu(models.Model):
	restaurant = models.ForeignKey(Restaurant,related_name="restaurant_menu")
	order = models.ForeignKey(Order, related_name='menu')
	menu = models.ForeignKey(Menu, related_name='order_menu')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)


	def __str__(self):
		return '{}'.format(self.menu.name)

	def get_cost(self):
		return self.price * self.quantity


'''
	TODO: When user exceeds purchase of something within a year he/she should be rewarded as Top Buyer of the year
'''