from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import  View
from django.views.generic import ListView, RedirectView, TemplateView, DetailView
from .models import RoomDetail, RoomImage, Amenitie, Room
from .forms import RoomForm, RoomDetailForm, RoomBookingForm


class AboutUsView(TemplateView):
    template_name = 'room/about_us.html'

class ContactUsView(TemplateView):
    template_name = 'room/contact_us.html'
    
class EventsView(TemplateView):
    template_name = 'room/events.html'
    
class ReservationView(TemplateView):
    template_name = 'room/reservation.html'
    
    
class HomeView(TemplateView):
    template_name = 'room/home.html'
    
# class RoomListView(TemplateView):
#     template_name = 'room/room_list.html'
#     context_object_name = 'rooms'

#     def get_context_data(self, **kwargs):
#         context = super(RoomListView, self).get_context_data(**kwargs)
#         room_details = RoomDetail.objects.select_related('room', 'image').all()
#         context['room_details'] = room_details
#         return context
    
#     def get_queryset(self):
#         print("RoomListView is called")
#         return super().get_queryset()

class RoomListView(ListView):
    model = RoomDetail  # Assuming you want to display details from RoomDetail
    template_name = 'room/test.html'
    context_object_name = 'room_details'

    def get_queryset(self):
        """
        Override the default queryset to filter rooms based on the room type.
        """
        
        room_type = self.kwargs.get('room_type')  # Get the room_type from the URL
        return RoomDetail.objects.filter(room_type=room_type).select_related('room', 'image')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_type'] = self.kwargs.get('room_type') 
        return context
    
class RoomDetailView(DetailView):
    model = RoomDetail
    template_name = 'room/test1.html'
    context_object_name = 'roomdetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_id = self.kwargs.get('pk')
        context['images'] = RoomImage.objects.filter(room__id=room_id)
        context['amenities'] = Amenitie.objects.filter(rooms__room__id=room_id)
        return context
    
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
    
def room_detail_view(request, room_type):
    # Fetch the room details based on the room type
    room_details = RoomDetail.objects.filter(room_type=room_type).first()
    images = None
    if room_details and room_details.image:
        # Assuming room_details.image points to a RoomImage instance
        images = [room_details.image.image1, room_details.image.image2, room_details.image.image3, room_details.image.image4, room_details.image.image5]
    
    context = {
        'room_details': room_details,
        'images': images,
    }
    return render(request, 'room_detail.html', context)