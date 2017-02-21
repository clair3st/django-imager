"""View API endpoint."""

from rest_framework import viewsets
from imager_images.models import Photo
from imager_api.serializers import PhotoSerializer
from django.urls import reverse_lazy


class PhotoViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    serializer_class = PhotoSerializer
    login_url = reverse_lazy("login")

    def get_queryset(self):
        """Get queryset for photographer."""
        return Photo.objects.filter(photographer=self.request.user.profile)
