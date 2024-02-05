from django.contrib import admin
from .models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_no', 'occupied']
    ordering = ['room_no']


@admin.register(RoomDetail)
class RoomDetailAdmin(admin.ModelAdmin):
    list_display = ['room', 'price', 'room_type', 'status', 'availability']
    list_editable = ['availability', ]
    ordering = ['price']
    list_filter = ['room_type', 'price', 'availability']
    search_fields = ['room_type', 'price']


@admin.register(Reservation)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'check_in', 'check_out', 'booking_date', 'updated_date']
    search_fields = ['user__username']
    # ordering = ['room']


admin.site.register(RoomImage)


@admin.register(BookingConfirmation)
class BookingConfirmationAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'get_email', 'room']
    search_fields = ['reservation__user__first_name', 'reservation__phone_number', 'reservation__user__email__iexact']

    def get_email(self, obj: BookingConfirmation) -> str:
        """Get the user email"""
        print(obj)
        return obj.reservation.user.email

    get_email.short_description = "Email"

    def get_full_name(self, obj: BookingConfirmation) -> str:
        """get the user full name"""
        return f"{obj.reservation.user.first_name} {obj.reservation.user.last_name}"

    get_full_name.short_description = "Full Name"
