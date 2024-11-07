from django.shortcuts import redirect, render
from django.views.generic.list import ListView

from web_app.forms import SatelliteForm
from web_app.models import Satellite


class SatelliteListView(ListView):
    model = Satellite
    queryset = Satellite.objects.all()
    context_object_name = "satellites"
    template_name = "satellites/satellite_list.html"


def satellite_view(request, pk):
    """
    Returns a rendered page with information about a single satellite.

    Args:
        request (Request): The HTTP request.
        pk (int): The primary key of the satellite.

    Returns:
        HttpResponse: The rendered page.
    """
    satellite = Satellite.objects.get(id=pk)
    return render(request, "satellites/satellite_view.html", {"satellite": satellite})

# CUD satellite

def add_satellite(request):
    """
    Returns a rendered page with the form for adding a new satellite.

    Args:
        request (Request): The HTTP request.

    Returns:
        HttpResponse: The rendered page.
    """
    if request.method == "GET":
        form = SatelliteForm()
        return render(request, "satellites/add_satellite.html", {"form": form})
    else:
        form = SatelliteForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.image = request.FILES["image"]
            form.save()
            return render(request, "satellites/satellite_added.html")
        else:
            return render(request, "satellites/add_satellite.html", {"form": form})


def change_satellite(request, pk):
    """
    Returns a rendered page with the form for changing a satellite.

    Args:
        request (Request): The HTTP request.
        pk (int): The primary key of the satellite.

    Returns:
        HttpResponse: The rendered page.
    """
    satellite = Satellite.objects.get(id=pk)

    if request.method == "GET":
        form = SatelliteForm(instance=satellite)
        return render(request, "satellites/change_satellite.html", {"form": form})
    else:
        form = SatelliteForm(request.POST, request.FILES, instance=satellite)
        if form.is_valid():
            form.save()
            return render(request, "satellites/satellite_changed.html")
        else:
            return render(request, "satellites/change_satellite.html", {"form": form})


def delete_satellite(request, pk):
    """
    Returns a rendered page with the form for deleting a satellite.

    Args:
        request (Request): The HTTP request.
        pk (int): The primary key of the satellite.

    Returns:
        HttpResponse: The rendered page.
    """
    satellite = Satellite.objects.get(id=pk)

    if request.method == "GET":
        return render(
            request,
            "satellites/delete_satellite.html",
            {"satellite": satellite},
        )
    else:
        satellite.delete()
        return redirect("satellite_list")


