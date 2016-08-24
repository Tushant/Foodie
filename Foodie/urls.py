"""foodie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('restaurants.urls', namespace='restaurants')),
    url(r'^review/', include('review.urls', namespace='review')),
    url(r'^userprofiles/', include('userprofiles.urls', namespace='userprofiles')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/restaurant/', include('restaurants.api.urls',namespace='restaurants-api')),
    url(r'^api/review/', include('review.api.urls',namespace='review-api')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)