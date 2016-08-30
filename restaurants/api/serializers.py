from rest_framework.serializers import (
								ModelSerializer, HyperlinkedIdentityField, HyperlinkedModelSerializer, 
								SerializerMethodField, StringRelatedField, ReadOnlyField
								)

from restaurants.models import ( Restaurant, OperatingTime, MenuCategory, 
								Menu, TimingChoice, FeatureChoice, Favorite
								)
from review.api.serializers import ReviewSeraializer
from review.models import Review
from restaurants.models import Menu, MenuCategory

from django.contrib.auth.models import User 



class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'username', 'email', 'is_staff')

class FeaturehoiceSerializer(ModelSerializer):
	class Meta:
		model = FeatureChoice


class TimingChoiceSerializer(ModelSerializer):
	class Meta:
		model = TimingChoice


class RestaurantSeraializer(ModelSerializer):
	owner = SerializerMethodField()
	features = FeaturehoiceSerializer(many=True)
	timings = TimingChoiceSerializer(many=True)
	class Meta:
		model = Restaurant
		read_only = ('id',)
		

	def get_owner(self, obj):
		print('get_owner obj is', obj)
		return str(obj.owner)

class RestaurantDetailSerializer(ModelSerializer):
	owner = SerializerMethodField()
	features = FeaturehoiceSerializer(many=True)
	timings = TimingChoiceSerializer(many=True)
	review = SerializerMethodField()
	menu = SerializerMethodField()
	class Meta:
		model = Restaurant
		read_only = ('id',)

	def get_owner(self, obj):
		return str(obj.owner)

	def get_review(self, obj):
		# content_type = obj.get_content_type
		# object_id = obj.id 
		review_qs = Review.objects.filter_by_instance(obj)
		review = ReviewSeraializer(review_qs, many=True).data 
		return review

	def get_menu(self, obj):
		print('obj',obj)
		restaurant = Restaurant.objects.get(slug=str(obj.slug))
		menu_qs = restaurant.menu_set.filter(available=True)
		print('menu_qs',menu_qs)
		menu = MenuSerializer(menu_qs, many=True).data
		return menu

	# def get_menu_category(self, obj):
	# 	restaurant = Restaurant.objects.get(slug=obj.slug)




class RestaurantCreateUpdateSerializer(ModelSerializer):
	owner = ReadOnlyField(source='owner.username')
	class Meta:
		model = Restaurant
		read_only = ('id',)
		fields = ('owner','name','address','city','phone_number','owner_email','opening_status','website','features','timings',
					'image','facebook_page','twitter_handle','other_details','is_parking','is_wifi',)

	# def validate(self, data):
	# 	print('data',data)
	# 	return data


class OperatingTimeSerializer(ModelSerializer):
	restaurant = RestaurantSeraializer(many=False)
	class Meta:
		model = OperatingTime

class OperatingTimeCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = OperatingTime
		read_only = ('id',)
		fields = ('restaurant','opening_time','closing_time','day_of_week',)

class MenuCategorySerializer(ModelSerializer):
	# menu = SerializerMethodField()
	class Meta:
		model = MenuCategory

	# def get_menu(self, obj):
	# 	menu_category = MenuCategory.objects.get(slug=obj.slug)
	# 	menu_qs = menu_category.menu.filter(available=True)
	# 	menu = MenuSerializer(menu_qs, many=True).data
	# 	return menu

class MenuSerializer(ModelSerializer):
	menu_category = MenuCategorySerializer(read_only=True, many=False)
	class Meta:
		model = Menu
		read_only = ('id',)

		# menu - > Restaurant
		# menu - > menu_category

class MenuCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Menu 
		read_only = ('id',)
		fields = ('menu_category','restaurant','name','image','description','price','stock','vote',)

