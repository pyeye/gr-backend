from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.text import slugify


class Menu(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey('Category', related_name='menu', verbose_name='Категория')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активированно')
    is_lunch = models.BooleanField(default=False, null=False, blank=True, verbose_name='Ланч')
    is_fire = models.BooleanField(default=False, null=False, blank=True, verbose_name='На огне')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    code = models.CharField(max_length=128, null=True, blank=True, verbose_name='Код')
    group = models.ForeignKey('Group', related_name='category', verbose_name='Группа')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активированно')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Group(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    code = models.CharField(max_length=128, null=False, unique=True, blank=False, verbose_name='Код')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Price(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True, related_name='prices', verbose_name='Меню')
    count = models.FloatField(null=True, blank=True, verbose_name='Количество (250/0.75)')
    measure = models.CharField(max_length=64, null=True, blank=True, verbose_name='Ед. измерения (гр./шт./л./мл./на чаше')
    value = models.IntegerField(null=False, blank=False, verbose_name='Цена')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимость'
