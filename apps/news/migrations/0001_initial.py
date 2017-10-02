# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-10 12:09
from __future__ import unicode_literals

import apps.news.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True, verbose_name='Дополнительно')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Созданно')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Обновленно')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активировано')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to=apps.news.models.upload_location, verbose_name='Изображение')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True, verbose_name='Дополнительно')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='news.Category', verbose_name='Категория')),
            ],
            options={
                'ordering': ['-updated_at'],
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]