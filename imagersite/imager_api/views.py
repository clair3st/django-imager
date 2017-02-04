"""View API endpoint."""

from rest_framework import viewsets, response, permissions
from imager_images.models import Photo
from imager_api.serializers import PhotoSerializer
from imager_api.permissions import IsOwnerOrReadOnly


class PhotoViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def list(self, request, *args, **kwargs):
        """Filter photos by user."""
        queryset = Photo.objects.filter(photographer=request.user.profile)
        serializer = PhotoSerializer(queryset, many=True)
        return response.Response(serializer.data)
