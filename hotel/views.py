from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView

from event.models import Event
from room.models import Room
from .models import Testimonial, BannerImage, History, VisionAndGoal
from .forms import ContactForm
from django.db.models import ImageField


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_event = Event.objects.order_by('-event_start')[:3]
        context['latest_event'] = latest_event
        return context


class AboutUsView(TemplateView):
    template_name = 'hotel/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonial'] = Testimonial.objects.all()
        context['history'] = History.objects.all()
        context['vision_goal'] = VisionAndGoal.objects.all()
        return context


class ContactUsView(FormView):
    template_name = 'hotel/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('hotel:contact')

    def form_valid(self, form):
        messages.success(self.request,
                         "We appreciate your inquiry and will respond promptly. Thank you for reaching out to us.")
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context


class RoomListView(ListView):
    model = Room
    template = 'room/rooms.html'
    context_object_name = 'rooms'


def footer_view(request):
    pass
