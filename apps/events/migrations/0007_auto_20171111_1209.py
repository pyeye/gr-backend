# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-11 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20170923_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
