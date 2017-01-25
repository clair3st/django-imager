"""Urls for images/ routes."""

from django.conf.urls import url

from imager_images.views import (
    PhotoList,
    LibraryView,
    AlbumList,
    PhotoDetail,
    AlbumDetail,
)

urlpatterns = [
    url(r'^library/$', LibraryView.as_view(), name='library'),
    url(r'^photos/$', PhotoList.as_view(), name='photo_list'),
    url(r'^albums/$', AlbumList.as_view(), name='album_list'),
    url(r'^photos/(?P<pk>\d+)$', PhotoDetail.as_view(), name='photo_detail'),
    url(r'^albums/(?P<pk>\d+)$', AlbumDetail.as_view(), name='album_detail'),
    url(r'^albums/add/$', AlbumList.as_view(), name='album_add'),
    url(r'^photos/add/$', AlbumList.as_view(), name='photo_add'),

]
