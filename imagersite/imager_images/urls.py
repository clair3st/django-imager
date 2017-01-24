"""Urls for images/ routes."""

from django.conf.urls import url

from imager_images.views import (
    PhotoList,
    library_view,
    AlbumList,
    photo_detail,
    album_detail,
)

urlpatterns = [
    url(r'^library/$', library_view, name='library'),
    url(r'^photos/$', PhotoList.as_view(), name='photo_list'),
    url(r'^albums/$', AlbumList.as_view(), name='album_list'),
    url(r'^photos/(?P<pk>\d+)$', photo_detail, name='photo_detail'),
    url(r'^albums/(?P<pk>\d+)$', album_detail, name='album_detail'),

]
