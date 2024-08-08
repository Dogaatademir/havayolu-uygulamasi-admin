from django.contrib import admin
from .models import Flight, Airport, Plane, Passenger, Airline

@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

# Plane modelinin sadece bir kez kaydedildiğinden emin olun
@admin.register(Plane)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ('model', 'capacity', 'airline','registration_number')
    list_filter = ('airline',)

# Mevcut diğer admin kayıtları
admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Passenger)
