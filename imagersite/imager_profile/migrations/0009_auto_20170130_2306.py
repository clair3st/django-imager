# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0008_merge_20170130_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='camera',
            field=models.CharField(blank=True, choices=[('CANON', 'Canon'), ('NIKON', 'Nikon'), ('OLYMPUS', 'Olympus'), ('SONY', 'Sony'), ('PANASONIC', 'Panasonic'), ('PHONE', 'Smart Phone'), ('', '---Camera Types---')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo_type',
            field=models.CharField(blank=True, choices=[('LANDSCAPE', 'Landscape'), ('BW', 'Black and White'), ('PORTRAIT', 'Portrait'), ('WEDDING', 'Wedding'), ('SPORTS', 'Sports'), ('WILDLIFE', 'Wildlife'), ('URBAN', 'Urban'), ('TRAVEL', 'Travel'), ('', '---Photography Styles---'), ('LE', 'Long Exposure')], max_length=255, null=True),
        ),
    ]
