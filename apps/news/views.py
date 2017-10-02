from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import NewsSerializer
from .models import News


class NewsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News.objects.all()
        return queryset
