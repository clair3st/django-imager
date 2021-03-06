"""Serializing and deserializing the photo instances into json."""

from rest_framework import serializers
from imager_images.models import Photo


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize Photo model data."""

    photographer = serializers.ReadOnlyField(source='photographer.username')

    class Meta:
        """Photo model and fields."""

        model = Photo
        fields = ('photographer', 'title', 'description', 'date_uploaded',
                  'date_modified', 'date_published', 'published', 'image_file')
