from django.contrib import admin

from user.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'is_active', 'created_at', 'updated_at', 'deleted_at']
    list_filter = ['is_active']
    search_fields = ['email']
