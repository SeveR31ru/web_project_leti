from django.shortcuts import render
from django.views.generic.list import ListView

from web_app.forms import SatelliteForm, TransmitterForm
from web_app.models import Satellite, Transmitter

# Create your views here.


def index(request):
    """
    Returns a rendered page with the main page of the web application.

    Args:
        request (Request): The HTTP request.
    """
    return render(request, "index.html")


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


class TransmitterListView(ListView):
    model = Transmitter
    queryset = Transmitter.objects.all()
    context_object_name = "transmitters"
    template_name = "transmitters/transmitter_list.html"


def transmitter_view(request, pk):
    """
    Returns a rendered page with information about a single transmitter.

    Args:
        request (Request): The HTTP request.
        pk (int): The primary key of the transmitter.

    Returns:
        HttpResponse: The rendered page.
    """
    transmitter = Transmitter.objects.get(id=pk)
    return render(
        request, "transmitters/transmitter_view.html", {"transmitter": transmitter}
    )


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


def add_transmitter(request):
    """
    Returns a rendered page with the form for adding a new transmitter.

    Args:
        request (Request): The HTTP request.

    Returns:
        HttpResponse: The rendered page.
    """
    if request.method == "GET":
        form = TransmitterForm()
        return render(request, "transmitters/add_transmitter.html", {"form": form})
    else:
        form = TransmitterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "transmitters/transmitter_added.html")
        else:
            return render(request, "transmitters/add_transmitter.html", {"form": form})
