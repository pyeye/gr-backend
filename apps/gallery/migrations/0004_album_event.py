# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-11 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20171111_1209'),
        ('gallery', '0003_auto_20171111_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='events.Event', verbose_name='Мероприятие'),
        ),
    ]
