"""URL patterns."""

from django.conf.urls import url
from imager_api.views import PhotoViewSet


urlpatterns = [
    url(
        r'^(?P<version>(v1))$',
        PhotoViewSet.as_view({'get': 'list'}), name='api_list'
    ),
]
