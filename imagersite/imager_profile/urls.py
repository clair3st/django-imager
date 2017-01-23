"""Url patterns for imager profile."""

from django.conf.urls import url
from imager_profile.views import (
    profile_view
)

urlpatterns = [
    url(r'^$', profile_view, name='my_profile'),

    url(r'^(?P<username>\w+)/$', profile_view, name='profile')
]
