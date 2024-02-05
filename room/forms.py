from datetime import date

from django import forms
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string

from core.settings import env
from .models import Room, RoomDetail, Reservation
from django.forms.widgets import SelectDateWidget, DateInput
from .exceptions import InvalidDateSelection


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_no']


class RoomDetailForm(forms.ModelForm):
    class Meta:
        model = RoomDetail
        fields = ['room', 'price', 'room_type', 'bed_type', 'availability', 'status', 'amenities']
        # widgets = 


class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Reservation
        fields = ['name', 'phone_number', 'check_in', 'check_out', 'email', 'adults', 'children', 'message',
                  'room_type', 'bed_type']
        widgets = {
            'check_in': DateInput(attrs={'type': 'date'}),
            'check_out': DateInput(attrs={'type': 'date'}),
        }

    def clean_check_in(self):
        """Validates the date i.e. check_in whether it precede the current date or not"""
        today = date.today()
        check_in = self.cleaned_data.get('check_in')
        if check_in < today:
            raise InvalidDateSelection("The selected check-out date must not precede the current date")
        return check_in

    def clean_check_out(self):
        """Validates the date i.e. check_out whether it precede the current date or not"""
        check_out = self.cleaned_data.get('check_out')
        if check_out < self.clean_check_in():
            raise InvalidDateSelection("The selected check-out date must not precede the current date")
        return check_out
