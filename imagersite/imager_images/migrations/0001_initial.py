# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 03:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imager_profile', '0005_auto_20170119_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(blank=True, null=True)),
                ('date_published', models.DateField(blank=True, null=True)),
                ('published', models.CharField(blank=True, choices=[('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public')], max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(blank=True, null=True)),
                ('date_published', models.DateField(blank=True, null=True)),
                ('published', models.CharField(blank=True, choices=[('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public')], max_length=255, null=True)),
                ('photographer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='imager_profile.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='contents',
            field=models.ManyToManyField(blank=True, null=True, related_name='in_album', to='imager_images.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='cover_photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='imager_images.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='imager_profile.UserProfile'),
        ),
    ]