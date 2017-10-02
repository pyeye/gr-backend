from rest_framework import serializers

from .models import Category, Instagram


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class InstagramSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Instagram
        fields = ('pk', 'short_code', 'img', 'likes', 'category', 'extra')
