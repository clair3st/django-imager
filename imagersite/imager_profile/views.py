"""Views for imager profile."""

from django.shortcuts import render
from imager_profile.models import UserProfile
from django.contrib.auth.models import User


# Create your views here
def profile_view(request, username):
    """Render profile view."""
    the_user = User.objects.get(username=username)
    profile = the_user.profile
    # photos = profile.photos.all()
    return render(request, 'imager_profile/profile.html', {'profile': profile})
