from django.contrib import admin

from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date', 'time','created_at', 'updated_at')
    search_fields = ('name', 'user__username', 'user__email')
    list_filter = ('date', 'user')
