from django import template

register = template.Library()

@register.filter(name='get_total_price')
def get_total_price(obj):
	return obj.get_cost()