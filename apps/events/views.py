from datetime import datetime, timedelta

from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import EventSerializer
from .models import Event


class EventViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.filter(
            is_active=True,
            date__gte=datetime.now(),
            date__lte=datetime.now() + timedelta(days=30)
        ).order_by('date')
        return queryset
