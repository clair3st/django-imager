from django.contrib import admin
from imager_images.models import Album, Photo


# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    """Display list for admin."""

    list_display = ("title", "description", "date_uploaded")


class PhotoAdmin(admin.ModelAdmin):
    """Display a list for Photos in Admin."""

    list_display = ("title", "description", "date_uploaded")

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
