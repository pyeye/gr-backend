from rest_framework import serializers

from .models import Menu, Price, Category, Group


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ('count', 'measure', 'value')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'code')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'code')


class MenuSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Menu
        fields = ('pk', 'name', 'description', 'category', 'is_fire', 'created_at', 'prices', 'extra')
