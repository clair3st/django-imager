"""Views for imager profile."""

from django.shortcuts import render
# from imager_profile.models import UserProfile
from django.contrib.auth.models import User
from imager_images.models import Photo, Album


# Create your views here
def profile_view(request, username):
    """Render profile view."""
    the_user = User.objects.get(username=username)
    profile = the_user.profile

    photo_data = Photo.objects.filter(photographer=the_user.profile)

    album_data = Album.objects.filter(owner=the_user.profile)

    data = {
        'photo_published': photo_data.filter(published="PUBLIC").count(),
        'photo_private': photo_data.filter(published="PRIVATE").count(),
        'album_published': album_data.filter(published="PUBLIC").count(),
        'album_private': album_data.filter(published="PRIVATE").count()
    }

    return render(request,
                  'imager_profile/profile.html',
                  {'profile': profile, 'data': data})
