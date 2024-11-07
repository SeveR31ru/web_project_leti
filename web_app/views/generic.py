from django.shortcuts import redirect, render
from django.views.generic.list import ListView

from web_app.forms import SatelliteForm, TleForm, TransmitterForm
from web_app.models import Satellite, Transmitter

# Create your views here.

# Satellite views


def index(request):
    """
    Returns a rendered page with the main page of the web application.

    Args:
        request (Request): The HTTP request.
    """
    return render(request, "index.html")


