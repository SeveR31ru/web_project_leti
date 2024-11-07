"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path

from web_app.views.generic import index
from web_app.views.satellite_views import (
    SatelliteListView,
    add_satellite,
    change_satellite,
    delete_satellite,
    satellite_view,
)
from web_app.views.tle_views import add_tle, calculate_sat_position
from web_app.views.transmitter_views import (
    TransmitterListView,
    add_transmitter,
    change_transmitter,
    delete_transmitter,
    transmitter_view,
)

BASE_URLS = [
    path("", index, name="index"),
    path("satellites", SatelliteListView.as_view(), name="satellite_list"),
    re_path(r"^satellites/(?P<pk>\d+)/$", satellite_view, name="satellite_view"),
    # add urls
    path("transmitters", TransmitterListView.as_view(), name="transmitter_list"),
    re_path(r"^transmitters/(?P<pk>\d+)/$", transmitter_view, name="transmitter_view"),
    # sat methods
    path("add_satellite", add_satellite, name="add_satellite"),
    re_path(
        r"^change_satellite/(?P<pk>\d+)/$",
        change_satellite,
        name="change_satellite",
    ),
    re_path(
        r"^delete_satellite/(?P<pk>\d+)/$",
        delete_satellite,
        name="delete_satellite",
    ),
    # transmitter methods
    path("add_transmitter", add_transmitter, name="add_transmitter"),
    re_path(
        r"^change_transmitter/(?P<pk>\d+)/$",
        change_transmitter,
        name="change_transmitter",
    ),
    re_path(
        r"^delete_transmitter/(?P<pk>\d+)/$",
        delete_transmitter,
        name="delete_transmitter",
    ),
    # tle methods
    path("add_tle", add_tle, name="add_tle"),
    path("get_coordinates/", calculate_sat_position, name="get_coordinates"),
]
