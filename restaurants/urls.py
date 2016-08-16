from django.conf.urls import url 

from . import views 

urlpatterns = [
	url(r'^$', views.home, name='homepage'),
	url(r'^add/', views.add_restaurant, name='add_restaurant')
]