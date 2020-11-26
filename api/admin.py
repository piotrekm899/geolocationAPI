from django.contrib import admin
from .models import (
    Connection,
    Currency,
    Geolocation,
    Language,
    Location,
    Security,
    TimeZone,
)


class GeolocationAdmin(admin.ModelAdmin):
    list_display = ('ip', 'type', 'city', 'timezone')


admin.site.register(Connection)
admin.site.register(Currency)
admin.site.register(Geolocation, GeolocationAdmin)
admin.site.register(Language)
admin.site.register(Location)
admin.site.register(Security)
admin.site.register(TimeZone)
