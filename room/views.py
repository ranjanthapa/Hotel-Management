from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import  View
from django.views.generic import ListView, RedirectView, TemplateView, DetailView
from .models import Room, RoomDetail, RoomBooking
from .forms import RoomForm, RoomDetailForm, RoomBookingForm


class HomeView(TemplateView):
    template_name = 'room/home.html'
    
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
        form = RoomBookingForm()
        return render(request, 'room/room_booking.html', {'form':form})
    def post(self, request, *args, **kwargs):
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            form.save()
        form = RoomBookingForm()
        return render(request, 'room/room_booking.html', {'form':form})