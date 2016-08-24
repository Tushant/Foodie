from rest_framework.serializers import (
								ModelSerializer, HyperlinkedIdentityField, HyperlinkedModelSerializer, 
								SerializerMethodField, StringRelatedField, ReadOnlyField
								)

from restaurants.models import ( Restaurant, OperatingTime, MenuCategory, 
								Menu, TimingChoice, FeatureChoice, Favorite
								)

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



class RestaurantCreateUpdateSerializer(ModelSerializer):
	owner = ReadOnlyField(source='owner.username')
	class Meta:
		model = Restaurant
		read_only = ('id',)
		fields = ('owner','name','address','city','phone_number','owner_email','opening_status','website','features','timings',
					'image','facebook_page','twitter_handle','other_details','is_parking','is_wifi',)


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
	class Meta:
		model = MenuCategory

class MenuSerializer(ModelSerializer):
	restaurant = RestaurantSeraializer(read_only=True, many=False)
	menu_category = MenuCategorySerializer(read_only=True, many=False)
	class Meta:
		model = Menu
		read_only = ('id',)

class MenuCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Menu 
		read_only = ('id',)
		fields = ('menu_category','restaurant','name','image','description','price','stock','vote',)

