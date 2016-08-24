from django.contrib import admin

from review.models import Review, Rate

admin.site.register(Review)
admin.site.register(Rate)