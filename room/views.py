from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import  View
from django.views.generic import ListView, RedirectView, TemplateView, DetailView
from .models import Room, RoomDetail, RoomBooking
from hotel.models import *
from .forms import RoomForm, RoomDetailForm, RoomBookingForm


class AboutUsView(TemplateView):
    template_name = 'room/about_us.html'

class ContactUsView(TemplateView):
    template_name = 'room/contact_us.html'
    
class EventsView(TemplateView):
    template_name = 'room/events.html'
    
class ReservationView(TemplateView):
    template_name = 'room/reservation.html'
    
    
# class HomeView(TemplateView):
#     template_name = 'room/home.html'
    
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
    
    
    
# class MenuListView(ListView):
#     model = MenuList
#     template_name = 'room/home.html'
#     context_object_name = 'menu_items'
    
    
    
# def home_and_menu(request):
#     menu_items = MenuList.objects.all()
#     bookings = RoomBooking.objects.all()
    
#     context = {
#         'menu_items': menu_items,
#         'bookings': bookings,
#     }

#     return render(request, 'room/home.html', context)


class HomeAndMenuView(ListView):
    template_name = 'room/home.html'
    context_object_name = 'menu_items'
    model = MenuList
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latestmenuimage'] = MenuImage.objects.latest('id')
        print(context)
        return context