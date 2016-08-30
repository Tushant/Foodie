from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User 

from rest_framework.serializers import (
								ModelSerializer, HyperlinkedIdentityField, HyperlinkedModelSerializer, 
								SerializerMethodField, StringRelatedField, ReadOnlyField, ValidationError
								)

# from restaurants.api.serializers import RestaurantSeraializer
from review.models import Review, Rate



def create_review_serializer(model_type='restaurant',slug=None, parent_id=None, reviewer=None):
	class ReviewCreateSerializer(ModelSerializer):
		class Meta:
			model = Review 
			fields = ('id','review','created',)

		def __init__(self, *args, **kwargs):
			self.model_type = model_type
			self.slug = slug 
			self.parent_obj = None 
			if parent_id:
				parent_qs = Review.objects.filter(id=parent_id)
				if parent_qs.exists() and parent_qs.count() == 1:
					self.parent_obj = parent_qs.first()
			return super(ReviewCreateSerializer, self).__init__(*args, **kwargs)

		def validate(self, data):
			model_type = self.model_type
			model_qs = ContentType.objects.filter(model=model_type)
			if not model_qs.exists() or model_qs.count() != 1:
				raise ValidationError('This is not a valid content type')
			SomeModel = model_qs.first().model_class()
			obj_qs = SomeModel.objects.filter(slug=self.slug) # Restaurant.objects.filter(slug=self.slug)
			if not obj_qs.exists() or obj_qs.count() != 1:
				raise ValidationError('This is not a slug for this content type')
			return data 

		def create(self, validated_data):
			review = validated_data.get('review')
			print('review',review)
			if reviewer:
				main_reviewer = reviewer
			else:
				main_reviewer = User.objects.all().first()
			model_type = self.model_type
			slug = self.slug 
			parent_obj = self.parent_obj
			review = Review.objects.create_for_model_type(model_type, slug, review, main_reviewer, parent_obj=parent_obj)
			return review

	return ReviewCreateSerializer

class ReviewSeraializerChild(ModelSerializer):
	reviewer = SerializerMethodField()
	class Meta:
		model = Review

	def get_reviewer(self, obj):
		return str(obj.reviewer)

class ReviewSeraializer(ModelSerializer):
	reply_count = SerializerMethodField()
	children = ReviewSeraializerChild(many=True)
	class Meta:
		model = Review
		read_only = ('id',)	
		fields = ('id','content_type','object_id','parent','review','children','reply_count','created')	

	def get_reply_count(self, obj):
		if obj.is_parent:
			return obj.children().count()
		return 0

	# def get_children(self, obj):
	# 	obj_children = []
	# 	if obj.is_parent:
	# 		return str(obj.children())
	# 		# for obj in obj.children():
	# 		# 	print(obj.review)
	# 		# 	obj_children.append(obj.review)
	# 		# return str(obj_children)
	# 	return None

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

