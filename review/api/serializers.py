from rest_framework.serializers import (
								ModelSerializer, HyperlinkedIdentityField, HyperlinkedModelSerializer, 
								SerializerMethodField, StringRelatedField, ReadOnlyField
								)

# from restaurants.api.serializers import RestaurantSeraializer
from review.models import Review, Rate

from django.contrib.auth.models import User 


class ReviewSeraializer(ModelSerializer):
	reply_count = SerializerMethodField()
	class Meta:
		model = Review
		read_only = ('id',)	
		fields = ('id','content_type','object_id','parent','review','reply_count','created')	

	def get_reply_count(self, obj):
		if obj.is_parent:
			return obj.children().count()
		return 0

	# def get_reviewer(self, obj):
	# 	print('get_user obj is', obj)
	# 	return str(obj.reviewer)


class ReviewChildSeraializer(ModelSerializer):
	# reviewer = SerializerMethodField()
	class Meta:
		model = Review
		read_only = ('id',)	
		fields = ('id','review','updated')

class ReviewDetailSeraializer(ModelSerializer):
	replies = SerializerMethodField()
	reply_count = SerializerMethodField()
	class Meta:
		model = Review
		read_only = ('id',)	
		fields = ('id','content_type','object_id','review','replies','reply_count','created')

	def get_replies(self,obj):
		if obj.is_parent:
			return ReviewChildSeraializer(obj.children(), many=True).data
		return None 

	def get_reply_count(self, obj):
		if obj.is_parent:
			return obj.children().count()
		return 0


class ReviewCreateUpdateSerializer(ModelSerializer):
	reviewer = ReadOnlyField(source='reviewer.username')
	class Meta:
		model = Review
		read_only = ('id',)
		fields = ('reviewer','content_type','object_id','content_object','parent','review',)

	def validate(self, data):
		print('data',data)
		return data


class RateSerializer(ModelSerializer):
	rater = SerializerMethodField()
	# restaurant = RestaurantSeraializer()
	class Meta:
		model = Rate
		read_only = ('id',)

	def get_rater(self, obj):
		return str(obj.rater)


class RateCreateUpdateSerializer(ModelSerializer):
	rater = ReadOnlyField(source='rater.username')
	class Meta:
		model = Rate
		read_only = ('id',)
		fields = ('rater','restaurant','rate',)

