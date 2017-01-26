"""View for website."""
from imager_images.models import Photo
from django.shortcuts import render


def home_view(request):
    """Home view callable, for the home page."""
    import random
    all_imgs = Photo.objects.filter(published="PUBLIC")

    try:
        random_img = random.choice(all_imgs)
    except IndexError:
        random_img = None

    return render(request, "imagersite/home.html", {'photo': random_img})
