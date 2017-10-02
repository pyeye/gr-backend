from rest_framework import serializers

from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('date', 'time_start', 'time_end', 'phone_number', 'email', 'name', 'sur_name', 'count_people', 'comment')
