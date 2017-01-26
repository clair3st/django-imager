"""Views for imager profile."""

from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    """Class based view for Profile page."""

    template_name = 'imager_profile/profile.html'

    def get_context_data(self, username=None):
        """Filter db for users data."""
        if username is None:
            username = self.request.user.username
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
        return {'profile': profile, 'data': data}
