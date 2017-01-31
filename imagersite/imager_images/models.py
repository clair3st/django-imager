"""Define image models."""

from django.db import models
from imager_profile.models import UserProfile
from django.utils.encoding import python_2_unicode_compatible

# Create yo  models here.

SHARING = (
    ('PRIVATE', "Private"),
    ('SHARED', "Shared"),
    ('PUBLIC', "Public"),
)


@python_2_unicode_compatible
class Photo(models.Model):
    """One individaul photo."""

    image_file = models.ImageField(upload_to="")
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)

    photographer = models.ForeignKey(UserProfile,
                                     related_name='photo',
                                     blank=True,
                                     null=True
                                     )

    published = models.CharField(max_length=255,
                                 choices=SHARING,
                                 default='PUBLIC')

    def __str__(self):
        """String representation of UserProfile."""
        return self.title


@python_2_unicode_compatible
class Album(models.Model):
    """Album class, one user, many photos."""

    owner = models.ForeignKey(UserProfile,
                              related_name="albums",
                              blank=True,
                              null=True
                              )

    contents = models.ManyToManyField(Photo,
                                      related_name='in_album',
                                      blank=True)

    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)

    published = models.CharField(max_length=255,
                                 choices=SHARING,
                                 default='PUBLIC')

    cover_photo = models.ForeignKey(Photo,
                                    related_name='cover',
                                    blank=True,
                                    null=True)
