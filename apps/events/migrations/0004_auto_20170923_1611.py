# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-23 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170923_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='showmen',
            field=models.ManyToManyField(blank=True, null=True, related_name='showmen', to='events.Showman', verbose_name='Ведущие'),
        ),
    ]
