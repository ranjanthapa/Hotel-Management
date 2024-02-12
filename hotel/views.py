from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView
from room.models import Room
from .models import Testimonial, BannerImage, History, VisionAndGoal
from .forms import ContactForm
from django.db.models import ImageField


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutUsView(TemplateView):
    template_name = 'hotel/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonial'] = Testimonial.objects.all()
        banner_image_instance = BannerImage.objects.first()
        if banner_image_instance:
            images = [getattr(banner_image_instance, field.name) for field in BannerImage._meta.fields if
                      isinstance(field, ImageField)]
            context['banner_images'] = images
        else:
            context['banner_images'] = None
        context['description'] = getattr(banner_image_instance, "description")
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


class EventsView(TemplateView):
    template_name = 'hotel/events.html'


class RoomListView(ListView):
    model = Room
    template = 'room/rooms.html'
    context_object_name = 'rooms'


def footer_view(request):
    pass
