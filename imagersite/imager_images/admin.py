from django.contrib import admin
from imager_images.models import Album, Photo


# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    """Display list for admin."""

    list_display = ("title", "description", "date_uploaded")

admin.site.register(Album, Photo)
