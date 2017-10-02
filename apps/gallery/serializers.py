from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from image_cropping.utils import get_backend

from apps.events.models import Event
from .models import Album, Image


class GalleryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'info', 'date')


class ImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='gallery_image')

    class Meta:
        model = Image
        fields = ('image', )


class AlbumSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField('get_crop_main_image')
    images = ImageSerializer(many=True, read_only=True)
    event = GalleryEventSerializer(read_only=True)

    def get_crop_main_image(self, obj):
        thumbnail_url = get_backend().get_thumbnail_url(
            obj.main_image,
            {
                'size': (600, 0),
                'box': obj.cropping,
                'crop': True,
                'quality': 95,
                'HIGH_RESOLUTION': True
            }
        )
        original_url = get_backend().get_thumbnail_url(
            obj.main_image,
            {
                'size': (1900, 0),
                'box': obj.cropping,
                'crop': True,
                'quality': 95,
                'HIGH_RESOLUTION': True

            }
        )
        return {'thumbnail': thumbnail_url, 'original': original_url}

    class Meta:
        model = Album
        fields = ('pk',  'event', 'main_image', 'images')


class GallerySerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField('get_images')
    image_count = serializers.IntegerField(source='images.count', read_only=True)
    event = GalleryEventSerializer(read_only=True)

    def get_images(self, obj):
        thumbnail_url = get_backend().get_thumbnail_url(
            obj.main_image,
            {
                'size': (600, 0),
                'box': obj.cropping,
                'crop': True,
                'quality': 95,
                'HIGH_RESOLUTION': True
            }
        )
        original_url = get_backend().get_thumbnail_url(
            obj.main_image,
            {
                'size': (1900, 0),
                'box': obj.cropping,
                'crop': True,
                'quality': 95,
                'HIGH_RESOLUTION': True

            }
        )
        return {'thumbnail': thumbnail_url, 'original': original_url}

    class Meta:
        model = Album
        fields = ('pk', 'event', 'main_image', 'image_count')
