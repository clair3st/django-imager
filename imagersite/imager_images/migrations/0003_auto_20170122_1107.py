# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 19:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_auto_20170122_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='published',
            field=models.CharField(blank=True, choices=[('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public'), ('', 'Select to share')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_modified',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2017, 1, 22, 11, 7, 46, 205771)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(upload_to='MEDIA'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='published',
            field=models.CharField(blank=True, choices=[('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public'), ('', 'Select to share')], max_length=255, null=True),
        ),
    ]