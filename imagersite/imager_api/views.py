"""View API endpoint."""

from rest_framework import viewsets, response, permissions, renderers
# from rest_framework.decorators import detail_route
# from rest_framework.response import Response
from imager_images.models import Photo
from imager_api.serializers import PhotoSerializer
from imager_api.permissions import IsOwnerOrReadOnly


class PhotoViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(photographer=self.request.user.profile)
