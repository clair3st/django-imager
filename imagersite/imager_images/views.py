"""Views for imager_images."""

from imager_images.models import Photo, Album
from django.views.generic import TemplateView


class LibraryView(TemplateView):
    """Class based view for Library."""

    template_name = 'imager_images/gallery.html'

    def get_context_data(self):
        """Show a users galleries and photos."""
        the_user = self.request.user
        user_photos = Photo.objects.filter(photographer=the_user.profile)
        user_albums = Album.objects.filter(owner=the_user.profile)
        context = {'albums': user_albums, 'photos': user_photos}
        return context


class AlbumList(TemplateView):
    """Class based view for Album list."""

    template_name = "imager_images/albums.html"

    def get_context_data(self):
        """Filter db for public albums."""
        albums = Album.objects.filter(published="PUBLIC")
        context = {'albums': albums}
        return context


class PhotoList(TemplateView):
    """Class based view for Photo list."""

    template_name = "imager_images/photos.html"

    def get_context_data(self):
        """Filter db for public photos."""
        photos = Photo.objects.filter(published="PUBLIC")
        context = {'photos': photos}
        return context


class PhotoDetail(TemplateView):
    """Class based view for Photo Detail."""

    template_name = "imager_images/photo_detail.html"

    def get_context_data(self, pk):
        """Show detail view of photo."""
        photo_id = Photo.objects.get(pk=pk)
        context = {'photos': photo_id}
        return context


class AlbumDetail(TemplateView):
    """Class based view for Album detail."""

    template_name = "imager_images/album_detail.html"

    def get_context_data(self, pk):
        """Show a list of all photos in an album."""
        album_id = Album.objects.filter(pk=pk)
        context = {'photos': album_id}
        return context
