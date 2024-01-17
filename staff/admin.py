from django.contrib import admin
from .models import Position, Staff

# Register the Position model
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register the Staff model
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'contact_number', 'address')
