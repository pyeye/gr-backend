from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import GallerySerializer, AlbumSerializer
from .models import Album


class AlbumViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def list(self, request, *args, **kwargs):
        queryset = Album.objects.all()
        serializer = GallerySerializer(queryset, many=True)
        return Response(serializer.data)

