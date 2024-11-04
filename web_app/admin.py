from django.contrib import admin

from web_app.models import Satellite, Tle, Transmitter

# Register your models here.


class SatelliteAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "identifier", "launch_date")


class TransmitterAdmin(admin.ModelAdmin):
    list_display = ("id", "satellite", "type")


class TleAdmin(admin.ModelAdmin):
    list_display = ("id", "satellite", "update_date")


admin.site.register(Satellite, SatelliteAdmin)
admin.site.register(Transmitter, TransmitterAdmin)
admin.site.register(Tle, TleAdmin)
