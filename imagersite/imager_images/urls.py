"""Urls for images/ routes."""

from django.conf.urls import url

from imager_images.views import (
    PhotoList,
    LibraryView,
    AlbumList,
    PhotoDetail,
    AlbumDetail,
    AlbumAdd,
    PhotoAdd,
    AlbumEdit,
    PhotoEdit,
    PhotoTagList,
)

urlpatterns = [
    url(r'^library/$', LibraryView.as_view(), name='library'),
    url(r'^photos/$', PhotoList.as_view(), name='photo_list'),
    url(r'^albums/$', AlbumList.as_view(), name='album_list'),
    url(r'^photos/(?P<pk>\d+)$', PhotoDetail.as_view(), name='photo_detail'),
    url(r'^albums/(?P<pk>\d+)$', AlbumDetail.as_view(), name='album_detail'),
    url(r'^albums/add/$', AlbumAdd.as_view(), name='album_add'),
    url(r'^photos/add/$', PhotoAdd.as_view(), name='photo_add'),
    url(r'^albums/(?P<pk>\d+)/edit/$', AlbumEdit.as_view(), name='album_edit'),
    url(r'^photos/(?P<pk>\d+)/edit/$', PhotoEdit.as_view(), name='photo_edit'),
    url(r'^albums/(?P<pk>\d+)/edit/$', AlbumEdit.as_view(), name='album_edit'),
    url(r'^photos/(?P<pk>\d+)/edit/$', PhotoEdit.as_view(), name='photo_edit'),
    url(r'^tagged/(?P<slug>[-\w]+)/$', PhotoTagList.as_view(), name='photo_tag'),
]
