from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from skyfield.api import EarthSatellite, load

from web_app.forms import TleForm
from web_app.models import Tle


class TleListView(ListView):
    """
    Returns a rendered page with the list of all TLEs.

    Attributes:
        model: The model of the list view. In this case, it is Tle.
        template_name: The template name of the list view. In this case, it is "tles/tle_list.html".
    """

    model = Tle
    template_name = "tles/tle_list.html"
    queryset = Tle.objects.all()
    context_object_name = "tles"


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


def tle_view(request, pk):
    """
    Returns a rendered page with the TLE with the given primary key.

    Args:
        request (Request): The HTTP request.
        pk (int): The primary key of the TLE.

    Returns:
        HttpResponse: The rendered page.
    """
    tle = Tle.objects.get(id=pk)
    return render(request, "tles/tle_view.html", {"tle": tle})


def change_tle(request, pk):
    """
    Returns a rendered page with the form for changing a TLE with the given primary key.

    Args:
        request (Request): The HTTP request.
        pk (int): The primary key of the TLE.

    Returns:
        HttpResponse: The rendered page.
    """
    tle = Tle.objects.get(id=pk)
    if request.method == "GET":
        form = TleForm(instance=tle)
        return render(request, "tles/change_tle.html", {"form": form})
    else:
        form = TleForm(request.POST, instance=tle)
        if form.is_valid():
            form.save()
            return render(request, "tles/tle_changed.html")
        else:
            return render(request, "tles/change_tle.html", {"form": form})


def delete_tle(request, pk):
    """
    Returns a rendered page with the form for deleting a TLE with the given primary key.

    Args:
        request (Request): The HTTP request.
        pk (int): The primary key of the TLE.

    Returns:
        HttpResponse: The rendered page.
    """
    tle = Tle.objects.get(id=pk)
    if request.method == "GET":
        return render(request, "tles/delete_tle.html", {"tle": tle})
    else:
        tle.delete()
        return redirect("tle_list")


@csrf_exempt
def calculate_sat_position(request):
    """
    Returns a JSON response with the current coordinates of the satellite with the given sat_id.

    The response contains the following keys:
        "lat": The latitude of the satellite in degrees.
        "lng": The longitude of the satellite in degrees.
        "alt": The altitude of the satellite in kilometers.

    Args:
        request (Request): The HTTP request. The request body should contain the sat_id of the satellite.

    Returns:
        JsonResponse: A JSON response with the current coordinates of the satellite.
    """

    sat_id = request.POST.get("sat_id")
    if Tle.objects.filter(satellite__id=sat_id).exists():
        tle = Tle.objects.filter(satellite__id=sat_id).first()
    else:
        return JsonResponse({}, status=404)
    try:
        ts = load.timescale()
        satellite = EarthSatellite(tle.tle_1, tle.tle_2, tle.tle_0, ts)
    except ValueError:
        return JsonResponse({"error": _("TLE is not valid")}, status=400)
    geocentric = satellite.at(ts.now())
    subpoint = geocentric.subpoint()
    coord_dict = {
        "alt": subpoint.elevation.km,
        "lat": subpoint.latitude.degrees,
        "lng": subpoint.longitude.degrees,
        "status_code": 200,
    }
    return JsonResponse(data=coord_dict, status=200)
