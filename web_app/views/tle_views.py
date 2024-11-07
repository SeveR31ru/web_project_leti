from django.shortcuts import render

from web_app.forms import TleForm


def add_tle(request):
    """
    Returns a rendered page with the form for adding a new TLE.

    Args:
        request (Request): The HTTP request.

    Returns:
        HttpResponse: The rendered page.
    """
    if request.method == "GET":
        form = TleForm()
        return render(request, "tles/add_tle.html", {"form": form})
    else:
        form = TleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "tles/tle_added.html")
        else:
            return render(request, "tles/add_tle.html", {"form": form})
