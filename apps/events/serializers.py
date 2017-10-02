from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from datetime import datetime

from .models import Event, Artist, Showman, EventArtistRel


class EventArtistSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='artist.name')
    style = serializers.ReadOnlyField(source='artist.style')
    img = VersatileImageFieldSerializer(source='artist.img', sizes='artist_img')


    class Meta:
        model = EventArtistRel
        fields = ('name', 'style', 'start', 'img')


class ArtistSerializer(serializers.ModelSerializer):
    img = VersatileImageFieldSerializer(sizes='artist_img')

    class Meta:
        model = Artist
        fields = ('name', 'style', 'img')


class ShowmanSerializer(serializers.ModelSerializer):
    img = VersatileImageFieldSerializer(sizes='showman_img')

    class Meta:
        model = Showman
        fields = ('name', 'img')


class EventSerializer(serializers.ModelSerializer):
    poster = VersatileImageFieldSerializer(sizes='event_poster')
    artists = EventArtistSerializer(source='eventartistrel_set', many=True)
    showmen = ShowmanSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('pk', 'name', 'artists', 'showmen', 'info', 'date', 'time',
                  'poster', 'extra')
