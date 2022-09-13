from django.contrib import admin

from flights.models.flights import Flights
from flights.models.airlines import Airlines


@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'airline', 'flight_number', 'departure', 'arrival', 'departure_time', 'arrival_time', 'price',
        'is_active')
    list_display_links = (
        'id', 'airline', 'flight_number', 'departure', 'arrival', 'departure_time', 'arrival_time', 'price',
        'is_active')
    list_filter = (
        'airline', 'flight_number', 'departure', 'arrival', 'departure_time', 'arrival_time', 'price', 'is_active')
    search_fields = (
        'airline', 'flight_number', 'departure', 'arrival', 'departure_time', 'arrival_time', 'price', 'is_active')
    list_per_page = 25


@admin.register(Airlines)
class AirlinesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id', 'name', 'is_active')
    list_filter = ('name', 'is_active')
    search_fields = ('name', 'is_active')
    list_per_page = 25
