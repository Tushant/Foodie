from django.conf.urls import include, url
from django.contrib import admin
from .views import (
    ReviewListAPIView, ReviewDetailAPIView, ReviewDestroyAPIView,
    ReviewCreateAPIView, ReviewUpdateAPIView,
    RateListAPIView, RateCreateAPIView, RateDetailAPIView,
     )

urlpatterns = [
    url(r'^$', ReviewListAPIView.as_view(), name="reviewlistapiview"),
    url(r'^create/$', ReviewCreateAPIView.as_view(), name="reviewcreateapiview"),
    url(r'^rate/$', RateCreateAPIView.as_view(), name="ratecreateapiview"),
    url(r'^ratelist/$', RateListAPIView.as_view(), name="ratelistapiview"),
    url(r'^rate/(?P<pk>\d+)/$', RateDetailAPIView.as_view(), name="ratedetailapiview"),
    url(r'^update/(?P<pk>\d+)$', ReviewUpdateAPIView.as_view(), name="reviewupdateapiview"),
    url(r'^delete/(?P<pk>\d+)$', ReviewDestroyAPIView.as_view(), name="reviewdeleteapiview"),
    url(r'^(?P<pk>\d+)/$', ReviewDetailAPIView.as_view(), name="reviewdetailapiview"),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


