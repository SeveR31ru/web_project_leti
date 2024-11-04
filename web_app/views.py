from django.shortcuts import render
from django.views.generic.list import ListView

from web_app.models import Satellite

# Create your views here.


def index(request):
    return render(request, "index.html")


class SatelliteListView(ListView):
    model = Satellite
    queryset = Satellite.objects.all()
    context_object_name = "satellites"
    template_name = "satellite_list.html"
