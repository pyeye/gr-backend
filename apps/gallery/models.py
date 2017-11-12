import uuid

from django.db import models
from django.dispatch import receiver
from django.contrib.postgres.fields import JSONField

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer
from image_cropping import ImageRatioField

from apps.events.models import Event


def upload_location(instance, filename):
    year, month, day = instance.created_at.year, instance.created_at.month, instance.created_at.day
    filename = uuid.uuid4().hex + '.jpg'
    return "gallery/{0}/{1}/{2}/{3}".format(year, month, day, filename)


def album_upload_location(instance, filename):
    year, month = instance.created_at.year, instance.created_at.month
    filename = uuid.uuid4().hex + '.jpg'
    return "album/{0}/{1}/{2}".format(year, month, filename)


class Album(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Событие')
    date = models.DateField(auto_now=False, null=False, blank=False, verbose_name='Дата')
    event = models.ForeignKey(Event, related_name='album', null=True, blank=True, verbose_name='Мероприятие')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активировано')
    main_image = models.ImageField(upload_to=album_upload_location, null=False, blank=False, verbose_name='Обложка')
    cropping = ImageRatioField('main_image', '100x100', free_crop=True, size_warning=True)
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['-date']


class Image(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='images', null=False, blank=False, verbose_name='Альбом')
    image = VersatileImageField(upload_to=upload_location, null=False, blank=False, verbose_name='Фото')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


@receiver(models.signals.post_save, sender=Image)
def warm_gallery_image_images(sender, instance, **kwargs):
    gallery_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='gallery_image',
        image_attr='image'
    )
    num_created, failed_to_create = gallery_img_warmer.warm()


@receiver(models.signals.post_save, sender=Album)
def warm_album_image_images(sender, instance, **kwargs):
    album_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='album_image',
        image_attr='main_image'
    )
    num_created, failed_to_create = album_img_warmer.warm()
