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
    description = models.CharField(max_length=255, blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(blank=True, null=True)
    date_published = models.DateField(blank=True, null=True)

    photographer = models.ForeignKey(UserProfile,
                                     related_name='photo',
                                     )

    published = models.CharField(max_length=255,
                                 choices=SHARING,
                                 blank=True,
                                 null=True)


@python_2_unicode_compatible
class Album(models.Model):
    """Album class, one user, many photos."""

    owner = models.ForeignKey(UserProfile,
                              related_name="albums",
                              )

    contents = models.ManyToManyField(Photo,
                                      related_name='in_album',
                                      blank=True,
                                      null=True)

    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(blank=True, null=True)
    date_published = models.DateField(blank=True, null=True)

    published = models.CharField(max_length=255,
                                 choices=SHARING,
                                 blank=True,
                                 null=True)

    cover_photo = models.OneToOneField(Photo,
                                       related_name='cover',
                                       blank=True,
                                       null=True)
