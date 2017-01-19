from django.db import models

# Create your models here.


class Photo(models.Model):
    """One individaul photo."""

    image_file = models.ImageField(upload_to="")
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(blank=True, null=True)
    date_published = models.DateField(blank=True, null=True)


class Album(models.Model):
    """Album class, one user, many photos."""

    pass
