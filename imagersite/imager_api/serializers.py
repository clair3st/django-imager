"""Serializing and deserializing the photo instances into json."""

from rest_framework import serializers
from imager_images.models import Photo


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize Photo model data."""

    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        """Photo model and fields."""

        model = Photo
        fields = ('title', 'description', 'date_uploaded', 'date_modified',
                  'date_published', 'published', 'image', 'photographer',
                  'tags', 'image_file')
