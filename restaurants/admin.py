from django.contrib import admin

from .models import Restaurant, MenuCategory, Menu, TimingChoice, FeatureChoice, OperatingTime, Favorite

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ['name','slug','address','city', 'opening_status', 'available', 'phone_number']
	prepopulated_fields = {'slug':('name',)}
	# list_fiter = ['available','created','updated']
	list_editable = ['phone_number', 'address', 'opening_status', 'available']

admin.site.register(Restaurant, RestaurantAdmin)

admin.site.register(TimingChoice)
admin.site.register(FeatureChoice)


class MenuCategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = { 'slug': ('name',) }

admin.site.register(MenuCategory,MenuCategoryAdmin)

class OperatingTimeAdmin(admin.ModelAdmin):
	list_display = ['restaurant','opening_time','closing_time','day_of_week']
admin.site.register(OperatingTime, OperatingTimeAdmin)


class MenuAdmin(admin.ModelAdmin):
	list_display = ['name','slug','price','vote','available','created','updated']
	list_filter = ['available','created','updated']
	list_editable = ['price', 'available']
	prepopulated_fields = { 'slug': ('name',) }

admin.site.register(Menu,MenuAdmin)
admin.site.register(Favorite)