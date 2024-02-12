from typing import Any

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import ListView, RedirectView, TemplateView, DetailView, FormView, CreateView

from core.settings import env
from .models import Room, RoomDetail, Reservation, BookingConfirmation
from .forms import RoomForm, RoomDetailForm, ReservationForm
from datetime import date
from .exceptions import InvalidDateSelection
from account.models import Account


class ReservationView(FormView):
    """performs the room reservation"""
    form_class = ReservationForm
    template_name = 'room/reservation.html'
    success_url = reverse_lazy('room:reservation')

    def form_valid(self, form):
        print("form valid method")

        room_number = self.room_selection(form.cleaned_data)

        user = Account.objects.filter(email=form.cleaned_data['email']).first()
        print(room_number)
        if user is None:
            messages.error(self.request, 'User needs to be register or login to reserver the room')
            return super().form_invalid(form)

        try:
            if room_number is not None:
                messages.success(self.request, f"An confirmation email has been sent to {form.cleaned_data['email']}")
                reservation = form.save(commit=False)
                reservation.user = self.request.user
                reservation.save()
                reservation_pk = reservation.pk
                print(f"reservation key{reservation_pk}")
                current_site = get_current_site(self.request)
                ReservationView.send_email(form.cleaned_data, current_site, room_number, reservation_pk)
            else:
                messages.add_message(self.request, message="Room not available", level=0)
                return super().form_valid(form)

        except InvalidDateSelection as e:
            print("handles the exception")
            messages.error(self.request, str(e))
            return self.form_invalid(form)

        response = super().form_valid(form)
        return response

    @staticmethod
    def send_email(valid_data: dict, domain, room_number: int, reservation: int) -> None:
        """send email"""
        print("Send method")
        name = valid_data.get('name')
        email = valid_data.get('email')

        file_path = 'account/email_verification.html'

        body = render_to_string(file_path, {
            'name': name,
            'uid': urlsafe_base64_encode(force_bytes(room_number)),
            'reservation_uid': urlsafe_base64_encode(force_bytes(reservation)),
            'domain': domain,
            # 'token': default_token_generator.make_token(user),
        })
        print("Email body:", body)

        email_from = env('HOST_USER')
        send_email = EmailMessage("Booking Confirmation", body, from_email=email_from, to=[email])
        try:
            send_email.send()
            print("Email sent successfully")
        except Exception as e:
            print(f"Error sending email: {e}")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    @staticmethod
    def is_in_range(room_check_in: date, room_check_out: date, new_check_in: date) -> bool:
        """checks if the room is available or not on a specific date"""
        if not room_check_in <= new_check_in <= room_check_out:
            return True

    @staticmethod
    def room_selection(valid_data: dict[str, Any]) -> int or None:
        room_details = RoomDetail.objects.filter(
            room_type=valid_data.get('room_type'),
            bed_type=valid_data.get('bed_type')
        )
        for room_detail in room_details:
            if room_detail.check_in is None and room_detail.check_out is None:
                return room_detail.room.room_no
            elif ReservationView.is_in_range(room_detail.check_in, room_detail.check_out, valid_data['check_in']):
                print(f"room detail room number{room_detail.room.room_no}")
                return room_detail.room.room_no

        return None


def confirm_booking(request, uidb64: str, res_uidb64: str):
    """ensure the confirmation for booking hotel room"""
    try:
        room_uid = urlsafe_base64_decode(uidb64).decode()
        print(room_uid)
        reservation_uid = urlsafe_base64_decode(res_uidb64).decode()
        print(reservation_uid)

    except (TypeError, ValueError, IntegrityError):
        print("none")
    room_obj = Room.objects.get(room_no=room_uid)
    room_obj.occupied = True
    reservation_obj = Reservation.objects.get(pk=reservation_uid)
    reservation_obj.availability = False
    booking_confirmation = BookingConfirmation.objects.create(reservation=reservation_obj)
    booking_confirmation.room.add(room_obj)
    messages.success(request, "The book confirmation succeed")
    return redirect('room:reservation')


class RoomDetailView(DetailView):
    model = Room
    template = 'room/room_detail.html'
    context_object_name = 'room'
