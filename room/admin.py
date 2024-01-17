from django.contrib import admin
from .models import *


@admin.register(Room)
class RoomAdminView(admin.ModelAdmin):
    ordering = ['room_no']


@admin.register(RoomDetail)
class RoomDetailAdminView(admin.ModelAdmin):
    list_display = ['room', 'price', 'room_type', 'status', 'availability']
    list_editable = ['availability', ]
    ordering = ['price']
    list_filter = ['room_type', 'price', 'availability']
    search_fields = ['room_type', 'price']


@admin.register(RoomBooking)
class RoomBookingAdminView(admin.ModelAdmin):
    list_display = ['user', 'room', 'check_in', 'check_out', 'booking_date', 'updated_date']
    search_fields = ['user__username']
    ordering = ['room']


admin.site.register(RoomImage)
admin.site.register(ContactUs)
admin.site.register(Goal)
admin.site.register(ReviewAndRating)
admin.site.register(AboutUs)
admin.site.register(MenuCategory)
admin.site.register(MenuList)

