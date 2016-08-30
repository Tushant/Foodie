from django.conf.urls import url 

from . import views 

urlpatterns = [
	# url(r'^$', views.home, name='homepage'),
	url(r'^restaurants/$', views.homepage, name='homepage'),
	url(r'^restaurant/(?P<restaurant_slug>[-\w]+)/$', views.restaurant_detail, name='restaurant_detail'),
	url(r'^favorite/$', views.FavoriteView.as_view(), name='favorite'),
	url(r'^add/', views.add_restaurant, name='add_restaurant'),
	url(r'^search/$', views.search_restaurant, name='search_restaurant'),
]