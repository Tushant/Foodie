from django import template

register = template.Library()

@register.filter
def get_total_price(obj):
	return obj.get_cost()