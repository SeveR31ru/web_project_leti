from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from skyfield.api import EarthSatellite, load

from web_app.forms import TleForm
from web_app.models import Tle


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
    ts = load.timescale()
    satellite = EarthSatellite(tle.tle_1, tle.tle_2, tle.tle_0, ts)
    geocentric = satellite.at(ts.now())
    subpoint = geocentric.subpoint()
    coord_dict = {
        "alt": subpoint.elevation.km,
        "lat": subpoint.latitude.degrees,
        "lng": subpoint.longitude.degrees,
        "status_code": 200,
    }
    return JsonResponse(data=coord_dict, status=200)
