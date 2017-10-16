"""maddog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from rest_framework import routers

from apps.events.views import EventViewSet
from apps.instagram.views import InstagramViewSet
from apps.news.views import NewsViewSet
from apps.menu.views import MenuViewSet, MenuBreakfastViewSet, CategoryAPIView
from apps.gallery.views import AlbumViewSet
from apps.reservation.views import ReservationAPIView


router = routers.SimpleRouter()
router.register(r'events', EventViewSet, base_name='api-events')
router.register(r'instagram', InstagramViewSet, base_name='api-instagram')
router.register(r'news', NewsViewSet, base_name='api-news')
router.register(r'menu', MenuViewSet, base_name='api-menu')
router.register(r'breakfast', MenuBreakfastViewSet, base_name='api-breakfast')
router.register(r'albums', AlbumViewSet, base_name='api-album')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/admin/', admin.site.urls),
    url(r'^api/v1/reservation/', ReservationAPIView.as_view()),
    url(r'^api/v1/category/menu/', CategoryAPIView.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^api/v1/__debug__/', include(debug_toolbar.urls)),
    ]
