from django.contrib import admin

from user.models.bookings import Bookings
from user.models.passengers import Passengers
from user.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'is_active', 'created_at', 'updated_at', 'deleted_at']
    list_filter = ['is_active']
    search_fields = ['email']


@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'flight', 'amount', 'created_at', 'updated_at', 'deleted_at']
    list_filter = ['user']
    search_fields = ['user']


@admin.register(Passengers)
class PassengersAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    list_filter = ['first_name']
    search_fields = ['first_name']
