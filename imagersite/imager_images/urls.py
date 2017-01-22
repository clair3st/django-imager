"""Urls for images/ routes."""

from django.conf.urls import url
from imager_images.views import (
    library_view,
    album_list,
    photo_list,
    photo_detail,
    album_detail,
)

urlpatterns = [
    url(r'^library/$', library_view, name='library'),
    url(r'^photos/$', photo_list, name='photo_list'),
    url(r'^albums/$', album_list, name='album_list'),
    url(r'^photos/(?P<pk>\d+)$', photo_detail, name='photo_detail'),
    url(r'^albums/(?P<pk>\d+)$', album_detail, name='album_detail'),

]
