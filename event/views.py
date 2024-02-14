from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Event


class EventView(ListView):
    template_name = 'event/events.html'
    paginate_by = 6
    model = Event
    context_object_name = 'events'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['events'] = Event.objects.all()
    #     print(Event.objects.all())
    #     return context


class EventDetailView(DetailView):
    template_name = 'event/event_detail.html'
    model = Event
    slug_field = 'slug'
    slug_url_kwarg = 'title'
    context_object_name = 'event'
