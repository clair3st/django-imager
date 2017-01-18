"""View for website."""

from django.shortcuts import render

def home_view(request):
    """Home view callable, for the home page."""
    return render(request, "imagersite/home.html")


# def test_view(request, num=None, word=None):
#         return render(request, "templates/")
