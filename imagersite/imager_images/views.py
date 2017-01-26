"""Views for imager_images."""

from django.shortcuts import render
from imager_images.models import Photo, Album


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


def photo_list(request):
    """Show a list of all public photos."""
    photos = Photo.objects.filter(published="PUBLIC")
    return render(request, 'imager_images/photos.html', {'photos': photos})


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
