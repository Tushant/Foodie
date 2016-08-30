from django.conf.urls import include, url
from django.contrib import admin
from .views import (
    RestaurantListAPIView, RestaurantDetailAPIView, 
    RestaurantCreateAPIView, RestaurantUpdateAPIView,
    OperatingTimeCreateAPIView, OperatingTimeUpdateAPIView,
    MenuListAPIView, MenuDetailAPIView, 
    MenuCreateAPIView, MenuUpdateAPIView, MenuCategoryDetailAPIView
                  )

urlpatterns = [
    url(r'^$', RestaurantListAPIView.as_view(), name="restaurantlistapiview"),
    url(r'^menu/$', MenuListAPIView.as_view(), name="menu_list_api"),
    url(r'^create/$', RestaurantCreateAPIView.as_view(), name="restaurantcreateapiview"),
    url(r'^update/(?P<slug>[\w-]+)$', RestaurantUpdateAPIView.as_view(), name="restaurantupdateapiview"),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailAPIView.as_view(), name="restaurantdetailapiview"),
    url(r'^menu/(?P<slug>[\w-]+)/$', MenuDetailAPIView.as_view(), name="menu_detail_api"),
    url(r'^menu_category/(?P<slug>[\w-]+)/$', MenuCategoryDetailAPIView.as_view(), name="menu_category_detail_api"),

    # menu post put
    url(r'^create/menu/$', MenuCreateAPIView.as_view(), name="menu_create_api"),
    url(r'^update/menu/(?P<slug>[\w-]+)$', MenuUpdateAPIView.as_view(), name="menu_update_api"),

    url(r'^create/operating_time/$', OperatingTimeCreateAPIView.as_view(), name="operatingtime_create_api"),
    url(r'^update/operating_time/(?P<pk>\d+)$', OperatingTimeUpdateAPIView.as_view(), name="operatingtime_update_api"),
 	   
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)