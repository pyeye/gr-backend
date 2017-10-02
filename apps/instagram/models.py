from django.db import models
from django.contrib.postgres.fields import JSONField

import requests


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False, verbose_name='Название')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Instagram(models.Model):
    category = models.ForeignKey('Category', related_name='category', verbose_name='Группа')
    short_code = models.CharField(max_length=255, null=True, unique=True, blank=True, verbose_name='Код')
    img = models.CharField(max_length=255, null=True, blank=True, verbose_name='Фото')
    likes = models.IntegerField(null=True, blank=True, verbose_name='Likes')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активированно')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.short_code

    class Meta:
        verbose_name = 'Instagram'
        verbose_name_plural = 'Instagram'

    def save(self, *args, **kwargs):
        payload = {'__a': '1'}
        url = 'https://www.instagram.com/p/' + str(self.short_code) + '/'
        r = requests.get(url, params=payload)
        json_response = r.json()
        self.img = json_response['graphql']['shortcode_media']['display_url']
        self.likes = json_response['graphql']['shortcode_media']['edge_media_preview_like']['count']
        self.extra['username'] = json_response['graphql']['shortcode_media']['owner']['username']
        self.extra['avatar'] = json_response['graphql']['shortcode_media']['owner']['profile_pic_url']

        super(Instagram, self).save(*args, **kwargs)



