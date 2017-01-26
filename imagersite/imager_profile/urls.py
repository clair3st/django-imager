"""Url patterns for imager profile."""

from django.conf.urls import url

from imager_profile.views import (
    ProfileView,
    ProfileEdit,
)

urlpatterns = [
    url(r'^edit/$', ProfileEdit.as_view(), name='profile_edit'),
    url(r'^$', ProfileView.as_view(), name='my_profile'),
    url(r'^(?P<username>\w+)/$', ProfileView.as_view(), name='profile'),
]
