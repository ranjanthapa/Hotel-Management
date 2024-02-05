from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import  View
from django.views.generic import ListView, RedirectView, TemplateView, DetailView
from .models import Room, RoomDetail, Reservation, Offers
from hotel.models import *
from .forms import RoomForm, RoomDetailForm, ReservationForm
from django.contrib import messages


class AboutUsView(TemplateView):
    template_name = 'room/about_us.html'
    
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['hotel_data'] = HotelData.objects.first()
        context['banners'] = HotelBanner.objects.first()
        return context

class ContactUsView(TemplateView):
    template_name = 'room/contact_us.html'
    
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['hotel_data'] = HotelData.objects.first()
        context['banners'] = HotelBanner.objects.first()
        context['reviews'] = ReviewAndRating.objects.all()
        return context
    
    
class EventsView(TemplateView):
    template_name = 'room/events.html'
    
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['events'] = Events.objects.all()
        context['banners'] = HotelBanner.objects.first()
        context['hotel_data'] = HotelData.objects.first()
        return context
    
    
class ReservationView(TemplateView):
    template_name = 'room/reservation.html'
    
    
# class HomeView(TemplateView):
#     template_name = 'room/home.html'
    
class RoomListView(ListView):
    model = RoomDetail
    template = 'room/rooms.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = RoomDetail.objects.filter(availability=True)
        context['banners'] = HotelBanner.objects.first()
        context['hotel_data'] = HotelData.objects.first()
        context['offers'] = Offers.objects.all()
        return context

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
    


class HomeAndMenuView(TemplateView):
    template_name = 'room/home.html'
    # context_object_name = 'menu_items'
    # model = MenuList
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['main_menu'] = MenuList.objects.filter(category__name='main').all()
        context['food_menu'] = MenuList.objects.filter(category__name='food').all()
        context['desserts_menu'] = MenuList.objects.filter(category__name='desserts').all()
        context['drinks_menu'] = MenuList.objects.filter(category__name='drinks').all()
        context['latestmenuimage'] = MenuImage.objects.latest('id')
        context['single_room'] = RoomDetail.objects.filter(room_type='single').first()
        context['family_room'] = RoomDetail.objects.filter(room_type='family').first()
        context['deluxe'] = RoomDetail.objects.filter(room_type='deluxe').first()
        context['president'] = RoomDetail.objects.filter(room_type='president').first()
        context['rooms'] = Room.objects.all()
        context['banners'] = HotelBanner.objects.first()
        context['reviews'] = ReviewAndRating.objects.all()
        context['events'] = Events.objects.all()
        context['hotel_data'] = HotelData.objects.first()
        print(context)
        return context
    
    
class CheckAvailability(View):
    def get(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        checkin_date = request.POST.get('checkin_date')
        checkout_date = request.POST.get('checkout_date')
        available_rooms = RoomDetail.objects.filter(availability=True)
        return render(request, 'room/available_rooms.html', {'available_rooms':available_rooms})
    
class BookRoom(View):
    def get(self, request, *args, **kwargs):
        pass
    def post(self, request, *args, **kwargs):
        room_id = request.POST.get('room_id')
        available_rooms = RoomDetail.objects.filter(availability=True)
        if available_rooms:
            for room in available_rooms:
                if room.room.id == room_id:
                    pass