from typing import Any

from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from django.views.generic import ListView, RedirectView, TemplateView, DetailView, FormView, CreateView

from core.settings import env
from .models import Room, RoomDetail, Reservation
from .forms import RoomForm, RoomDetailForm, ReservationForm
from datetime import date
from .exceptions import InvalidDateSelection


class AboutUsView(TemplateView):
    template_name = 'hotel/about_us.html'


class ContactUsView(TemplateView):
    template_name = 'hotel/contact_us.html'


class EventsView(TemplateView):
    template_name = 'room/events.html'


class ReservationView(FormView):
    """performs the room reservation"""
    form_class = ReservationForm
    template_name = 'room/reservation.html'
    success_url = reverse_lazy('room:reservation')

    def form_valid(self, form):
        print("form valid method")
        try:
            room = self.room_selection(new_check_in=form.cleaned_data['check_in'])
            print(room)
            if room is not None:
                messages.success(self.request, "An confirmation email has been sent to you")
                ReservationView.send_email(form.cleaned_data)
            else:
                messages.add_message(self.request, "Room not available")
                return super().form_valid(form)

        except InvalidDateSelection:
            print("handles the exception")
            messages.error(self.request, "The selected date must not precede the current date")
            return self.form_invalid(form)

        response = super().form_valid(form)
        return response

    @staticmethod
    def send_email(valid_data: dict) -> None:
        """send email"""
        print("Send method")
        name = valid_data.get('name')
        email = valid_data.get('email')
        request = HttpRequest()
        current_site = get_current_site(request)

        file_path = 'account/email_verification.html'
        print(name, email)
        body = render_to_string(file_path, {
            'name': name,
            'uid': "123",
            'domain': current_site,
            'payment_url': "https://www.instagram.com",
            "confirm_url": "https://www.facebook.com"
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
        # return False

    @staticmethod
    def room_selection(new_check_in: date) -> dict[str, Any]:
        """select the available room"""
        print('inside of room_selection method')
        room_details: QuerySet = RoomDetail.objects.values('room', 'check_in', 'check_out').all()
        print(room_details)
        for detail in room_details:
            if detail['check_in'] or detail['check_out'] is None:
                return detail

            if ReservationView.is_in_range(room_check_in=detail['check_in'], room_check_out=detail['check_out'],
                                           new_check_in=new_check_in):
                print(detail)
                return detail


def confirm_booking(request):
    pass


class HomeView(TemplateView):
    template_name = 'home.html'


class RoomListView(ListView):
    model = Room
    template = 'room/rooms.html'
    context_object_name = 'rooms'


class RoomDetailView(DetailView):
    model = Room
    template = 'room/room_detail.html'
    context_object_name = 'room'


class RoomBookView(View):
    def get(self, request, *args, **kwargs):
        form = ReservationForm()
        return render(request, 'room/room_booking.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
        form = ReservationForm()
        return render(request, 'room/room_booking.html', {'form': form})
