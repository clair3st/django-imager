"""Views for imager_images."""

from django.shortcuts import render
from imager_images.models import Photo, Album
from django.views.generic import TemplateView


def library_view(request):
    """Show a users galleries and photos."""
    the_user = request.user
    user_photo = Photo.objects.filter(photographer=the_user.profile)
    user_album = Album.objects.filter(owner=the_user.profile)
    return render(request,
                  'imager_images/gallery.html',
                  {'albums': user_album, 'photos': user_photo})


def album_list(request):
    """Show a list of all public albums."""
    albums = Album.objects.filter(published="PUBLIC")
    return render(request, 'imager_images/albums.html', {'albums': albums})


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


def photo_detail(request, pk):
    """Show detail view of a photo."""
    photo_id = Photo.objects.get(pk=pk)
    return render(request,
                  'imager_images/photo_detail.html',
                  {'photo': photo_id})


def album_detail(request, pk):
    """Show a list of all photos in an album."""
    album_id = Album.objects.get(pk=pk)
    return render(request,
                  'imager_images/album_detail.html',
                  {'album': album_id})
