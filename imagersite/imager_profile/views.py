"""Views for imager profile."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from imager_images.models import Photo, Album
from imager_profile.models import UserProfile
from imager_profile.forms import UserProfileForm


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


class ProfileEdit(LoginRequiredMixin, UpdateView):
    """Update profile and user info."""

    login_required = True
    template_name = 'imager_profile/profile_edit.html'
    success_url = reverse_lazy('my_profile')
    form_class = UserProfileForm
    model = UserProfile
    login_url = reverse_lazy("login")

    def get_object(self):
        """Get the logged in user to edit."""
        return self.request.user.profile

    def form_valid(self, form):
        """Save object after post."""
        self.object = form.save()
        self.object.user.first_name = form.cleaned_data['First Name']
        self.object.user.last_name = form.cleaned_data['Last Name']
        self.object.user.email = form.cleaned_data['Email']
        self.object.user.save()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
