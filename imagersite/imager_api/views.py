"""View API endpoint."""

from rest_framework import viewsets, permissions
from imager_images.models import Photo
from imager_api.serializers import PhotoSerializer
from imager_api.permissions import IsOwnerOrReadOnly


class PhotoViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def get_queryset(self):
        """Get queryset for photographer."""
        return Photo.objects.filter(photographer=self.request.user.profile)
