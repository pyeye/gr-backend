from rest_framework import viewsets, generics
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import MenuSerializer, CategorySerializer
from .models import Menu, Category
from apps.base.renderers import GRMenuRenderer


class MenuViewSet(viewsets.ReadOnlyModelViewSet):

    LUNCH_GROUP = 'lunch'

    serializer_class = MenuSerializer
    renderer_classes = (GRMenuRenderer, JSONRenderer, BrowsableAPIRenderer)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """

        group = self.request.query_params.get('group', None)
        if group is not None:

            if group == self.LUNCH_GROUP:
                queryset = Menu.objects.filter(is_lunch=True)
            else:
                queryset = Menu.objects.filter(is_active=True, category__group__code=group)

        return queryset


class CategoryAPIView(generics.ListAPIView):

    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Category.objects.filter(is_active=True)
        group = self.request.query_params.get('group', None)
        if group is not None:
            queryset = queryset.filter(group__code=group)
        return queryset

