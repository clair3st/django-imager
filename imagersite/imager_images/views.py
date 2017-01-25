"""Views for imager_images."""

from imager_images.models import Photo, Album
from django.views.generic import ListView, DetailView


class LibraryView(ListView):
    """Class based view for Library."""

    template_name = 'imager_images/gallery.html'

    def get_queryset(self):
        """Get public albums."""
        return {}

    def get_context_data(self):
        """Show a users galleries and photos."""
        the_user = self.request.user
        user_photos = Photo.objects.filter(photographer=the_user.profile)
        user_albums = Album.objects.filter(owner=the_user.profile)
        context = {'albums': user_albums, 'photos': user_photos}
        return context


class AlbumList(ListView):
    """Class based view for Album list."""

    template_name = "imager_images/albums.html"
    model = Album
    context_object_name = 'albums'

    def get_queryset(self):
        """Get public albums."""
        return Album.objects.filter(published="PUBLIC")


class PhotoList(ListView):
    """Class based view for Photo list."""

    template_name = "imager_images/photos.html"
    model = Photo
    context_object_name = 'photos'

    def get_queryset(self):
        """Get public photos."""
        return Photo.objects.filter(published="PUBLIC")


class PhotoDetail(DetailView):
    """Class based view for Photo Detail."""

    template_name = "imager_images/photo_detail.html"
    model = Photo


class AlbumDetail(DetailView):
    """Class based view for Album detail."""

    template_name = 'imager_images/album_detail.html'
    model = Album
