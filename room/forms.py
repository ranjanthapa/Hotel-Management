from django import forms
from .models import Room, RoomDetail, RoomBooking


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_no']

class RoomDetailForm(forms.ModelForm):
    class Meta:
        model = RoomDetail
        fields = ['room', 'price', 'room_type', 'bed_type', 'availability', 'status', 'amenities']
        # widgets = 

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = ['adults', 'children', 'check_in', 'check_out']