from django.conf.urls import url 

from . import views 

urlpatterns = [
	url(r'^profile/(?P<profile_slug>[-\w]+)/$', views.profile, name='profile'),
	# url(r'^profile/(?P<profile_slug>[-\w]+)/$', UserProfileDetailView.as_view(), name='profile_view'),

]