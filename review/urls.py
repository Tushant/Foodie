from django.conf.urls import url

from .models import Review, Rate 

from . import views


urlpatterns = [
	# url(r'^$', views.review_list, name='review_list'),
 #    url(r'^(?P<review_id>\d+)/$', views.review_detail, name='review_detail'),
 	url(r'^(?P<review_id>\d+)/$', views.review_thread, name='thread'),	
    url(r'^add/(?P<review_id>\d+)/$', views.add_review, name='add_review'),
]

