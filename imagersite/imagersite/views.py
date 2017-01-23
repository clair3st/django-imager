"""View for website."""
from imager_images.models import Photo
from django.shortcuts import render
from random import randint


def home_view(request):
    """Home view callable, for the home page."""
    import pdb; pdb.set_trace()
    all_imgs = Photo.objects.filter(published="PUBLIC")
    img_len = len(all_imgs)
    img_num = randint(1, img_len)
    try:
        random_img = all_imgs[img_num] - 1
    except IndexError:
        random_img = all_imgs[7]
    return render(request, "imagersite/home.html", {'photo': random_img})
