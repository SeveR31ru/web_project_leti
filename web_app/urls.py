"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path

from web_app import views

BASE_URLS = [
    path("", views.index, name="index"),
    path("satellites", views.SatelliteListView.as_view(), name="satellite_list"),
    re_path(r"^satellites/(?P<pk>\d+)/$", views.satellite_view, name="satellite_view"),
    # add urls
    path("transmitters", views.TransmitterListView.as_view(), name="transmitter_list"),
    re_path(
        r"^transmitters/(?P<pk>\d+)/$", views.transmitter_view, name="transmitter_view"
    ),
    path("add_satellite", views.add_satellite, name="add_satellite"),
    path("add_transmitter", views.add_transmitter, name="add_transmitter"),
    path("add_tle", views.add_tle, name="add_tle"),
]
