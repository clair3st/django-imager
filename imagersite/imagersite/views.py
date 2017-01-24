"""View for website."""
from imager_images.models import Photo
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Class based view for home page."""

    template_name = "imagersite/home.html"

    def get_context_data(self):
        """Filter db for a random background."""
        import random
        all_imgs = Photo.objects.filter(published="PUBLIC")

        try:
            random_img = random.choice(all_imgs)
        except IndexError:
            random_img = None

        return {'photo': random_img}
