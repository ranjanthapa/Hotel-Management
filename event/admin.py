from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdminView(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
