from django.shortcuts import render

def home_view(request):
    """Home view callable, for the home page."""
    template = loader.get_template("imagersite/home.html")
    response = template.render()
    return render(request, "templates/home.html", {"variable": "value"})


def test_view(request, num=None, word=None):
        return render(request, "templates/")