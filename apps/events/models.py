import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


def upload_location(instance, filename):
    year, month = instance.date.year, instance.date.month
    filename = uuid.uuid4().hex + '.jpg'
    return "events/{0}/{1}/{2}".format(year, month, filename)


def artists_upload_location(instance, filename):
    name = slugify(instance.name, allow_unicode=True)
    filename = uuid.uuid4().hex + '.jpg'
    return "artists/{0}/{1}".format(name, filename)

def showman_upload_location(instance, filename):
    name = slugify(instance.name, allow_unicode=True)
    filename = uuid.uuid4().hex + '.jpg'
    return "showman/{0}/{1}".format(name, filename)


class Event(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
    artists = models.ManyToManyField('Artist', through='EventArtistRel',  blank=True, related_name='artists', verbose_name='Артисты')
    showmen = models.ManyToManyField('Showman', blank=True, related_name='showmen', verbose_name='Ведущие')
    info = models.TextField(null=True, blank=True, verbose_name='Дополнительная информация')
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    time = models.TimeField(null=True, blank=True, verbose_name='Время')
    created_at = models.DateTimeField(auto_now=True, null=False, blank=True, verbose_name='Созданно')
    is_active = models.BooleanField(default=True, null=False, blank=True, verbose_name='Активировано')
    poster = VersatileImageField(upload_to=upload_location, null=True, blank=True, verbose_name='Афиша')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Artist(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name='Название')
    style = models.CharField(max_length=255, null=False, blank=False, verbose_name='Стиль')
    img = VersatileImageField(upload_to=artists_upload_location, null=True, blank=True, verbose_name='Фото')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'


class Showman(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name='Название')
    img = VersatileImageField(upload_to=showman_upload_location, null=True, blank=True, verbose_name='Фото')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ведущий'
        verbose_name_plural = 'Ведущие'


class EventArtistRel(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start = models.TimeField(null=False, blank=False, verbose_name='Начало')
    extra = JSONField(blank=True, null=True, default={}, verbose_name='Дополнительно')



@receiver(models.signals.post_save, sender=Event)
def warm_event_poster_images(sender, instance, **kwargs):
    event_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='event_poster',
        image_attr='poster'
    )
    num_created, failed_to_create = event_img_warmer.warm()

@receiver(models.signals.post_save, sender=Artist)
def warm_artist_images(sender, instance, **kwargs):
    artist_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='artist_img',
        image_attr='img'
    )
    num_created, failed_to_create = artist_img_warmer.warm()


@receiver(models.signals.post_save, sender=Showman)
def warm_showman_images(sender, instance, **kwargs):
    showman_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='showman_img',
        image_attr='img'
    )
    num_created, failed_to_create = showman_img_warmer.warm()
