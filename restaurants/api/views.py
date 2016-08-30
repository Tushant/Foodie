from django.db.models import Q

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import (
		RestaurantSeraializer, RestaurantCreateUpdateSerializer, RestaurantDetailSerializer, MenuSerializer,
		MenuCategorySerializer, MenuCreateUpdateSerializer, OperatingTimeCreateUpdateSerializer, MenuCategorySerializer
		)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly 

# from .paginations import RentalLimitOffsetPagination, RentalPageNumberPagination
# from .permissions import IsOwnerOrReadOnly

from restaurants.models import ( Restaurant, OperatingTime, MenuCategory, 
								Menu, TimingChoice, FeatureChoice, Favorite
								)


class RestaurantListAPIView(ListAPIView):
	serializer_class = RestaurantSeraializer

	def get_queryset(self, *args, **kwargs):
		queryset = Restaurant.objects.all()
		return queryset

class RestaurantDetailAPIView(RetrieveAPIView):
	serializer_class = RestaurantDetailSerializer
	queryset = Restaurant.objects.all() 
	lookup_field = 'slug'

class RestaurantCreateAPIView(CreateAPIView):
	serializer_class = RestaurantCreateUpdateSerializer
	queryset = Restaurant.objects.all()
	parser_classes = (FormParser,MultiPartParser,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class RestaurantUpdateAPIView(RetrieveUpdateAPIView):
	serializer_class = RestaurantCreateUpdateSerializer
	queryset = Restaurant.objects.all()
	parser_classes = (FormParser,MultiPartParser,)
	lookup_field = 'slug'

class RestaurantDestroyAPIView(DestroyAPIView):
	serializer_class = RestaurantCreateUpdateSerializer
	queryset = Restaurant.objects.all()
	lookup_field = 'slug'

class OperatingTimeCreateAPIView(CreateAPIView):
	serializer_class = OperatingTimeCreateUpdateSerializer
	queryset = OperatingTime.objects.all()
	parser_classes = (FormParser,MultiPartParser,)

class OperatingTimeUpdateAPIView(RetrieveUpdateAPIView):
	serializer_class = OperatingTimeCreateUpdateSerializer
	queryset = OperatingTime.objects.all()
	parser_classes = (FormParser,MultiPartParser,)
	lookup_field = 'pk'

class MenuListAPIView(ListAPIView):
	serializer_class = MenuSerializer

	def get_queryset(self, *args, **kwargs):
		queryset = Menu.objects.all()
		return queryset

class MenuDetailAPIView(RetrieveAPIView):
	serializer_class = MenuSerializer
	queryset = Menu.objects.all()
	lookup_field = 'slug'

class MenuCreateAPIView(CreateAPIView):
	serializer_class = MenuCreateUpdateSerializer
	queryset = Menu.objects.all()
	parser_classes = (FormParser,MultiPartParser,)

class MenuUpdateAPIView(RetrieveUpdateAPIView):
	serializer_class = MenuCreateUpdateSerializer
	queryset = Menu.objects.all()
	lookup_field = 'slug'
	parser_classes = (FormParser,MultiPartParser,)

class MenuCategoryDetailAPIView(RetrieveAPIView):
	serializer_class = MenuCategorySerializer
	queryset = MenuCategory.objects.all()
	lookup_field = 'slug'
