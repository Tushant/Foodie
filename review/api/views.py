from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import (
		ReviewSeraializer, ReviewCreateUpdateSerializer, ReviewDetailSeraializer,
		RateSerializer, RateCreateUpdateSerializer
		)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly 

# from .paginations import RentalLimitOffsetPagination, RentalPageNumberPagination
# from .permissions import IsOwnerOrReadOnly

from review.models import Review, Rate


class ReviewListAPIView(ListAPIView):
	serializer_class = ReviewSeraializer
	filter_backends = [SearchFilter, OrderingFilter]
	def get_queryset(self, *args, **kwargs):
		queryset_list = Review.objects.all()
		query = self.request.GET.get('q')
		if query:
			queryset_list = queryset_list.filter(
					Q(review__icontains=query)|
					Q(user__first_name__icontains=query)|
					Q(user__last_name__icontains=query)
				).distinct()
		return queryset_list

class ReviewDetailAPIView(RetrieveAPIView):
	serializer_class = ReviewDetailSeraializer
	queryset = Review.objects.all() 
	lookup_field = 'pk'

class ReviewCreateAPIView(CreateAPIView):
	serializer_class = ReviewCreateUpdateSerializer
	queryset = Review.objects.all()
	parser_classes = (FormParser,MultiPartParser,)

	def perform_create(self, serializer):
		print('serializer',serializer)
		print('self',self)
		print('self.request',self.request.user)
		serializer.save(reviewer=self.request.user)

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(ReviewCreateAPIView, self).dispatch(request, *args, **kwargs)

class ReviewUpdateAPIView(RetrieveUpdateAPIView):
	serializer_class = ReviewCreateUpdateSerializer
	queryset = Review.objects.all()
	parser_classes = (FormParser,MultiPartParser,)
	lookup_field = 'pk'

class ReviewDestroyAPIView(DestroyAPIView):
	serializer_class = ReviewCreateUpdateSerializer
	queryset = Review.objects.all()
	lookup_field = 'pk'

class RateListAPIView(ListAPIView):
	serializer_class = RateSerializer

	def get_queryset(self, *args, **kwargs):
		queryset = Rate.objects.all()
		return queryset

class RateDetailAPIView(RetrieveAPIView):
	serializer_class = RateSerializer
	queryset = Rate.objects.all()
	lookup_field = 'pk'

class RateCreateAPIView(CreateAPIView):
	serializer_class = RateCreateUpdateSerializer
	queryset = Rate.objects.all()
	# parser_classes = (FormParser,MultiPartParser,)

	def perform_create(self, serializer):
		serializer.save(rater=self.request.user)


class RateUpdateAPIView(RetrieveUpdateAPIView):
	serializer_class = RateCreateUpdateSerializer
	queryset = Rate.objects.all()
	parser_classes = (FormParser,MultiPartParser,)
	lookup_field = 'pk'


