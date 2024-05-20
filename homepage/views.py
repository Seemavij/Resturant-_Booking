ffrom django.shortcuts import render
from .models import home


def about_me(request):
    """
    Renders the home page
    """
    home = home.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "home/home.html",
        {"home": home},
    )

