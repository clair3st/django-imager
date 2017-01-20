# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0004_auto_20170117_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='camera',
            field=models.CharField(blank=True, choices=[('CANNON', 'Cannon'), ('NIKON', 'Nikon'), ('OLYMPUS', 'Olympus'), ('SONY', 'Sony'), ('PANASONIC', 'Panasonic'), ('PHONE', 'Phone')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo_type',
            field=models.CharField(blank=True, choices=[('LANDSCAPE', 'Landscape'), ('BW', 'Black and White'), ('PORTRAIT', 'Portrait'), ('WEDDING', 'Wedding'), ('SPORTS', 'Sports'), ('WILDLIFE', 'Wildlife'), ('URBAN', 'Urban'), ('TRAVEL', 'Travel')], max_length=255, null=True),
        ),
    ]
