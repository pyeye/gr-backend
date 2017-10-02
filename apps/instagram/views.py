from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import InstagramSerializer
from .models import Instagram


class InstagramViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = InstagramSerializer

    def get_queryset(self):
        queryset = Instagram.objects.all()
        return queryset
