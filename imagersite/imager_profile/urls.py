"""Url patterns for imager profile."""

from django.conf.urls import url
from django.views.generic import TemplateView

from imager_profile.views import (
    profile_view
)

urlpatterns = [
    url(r'^$', profile_view, name='my_profile'),

    url(r'^(?P<username>\w+)/$',
        TemplateView.as_view(template_name="imager_profile/profile.html"),
        name='profile')
]
