from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import  View
from django.views.generic import ListView, RedirectView, TemplateView


class HomeView(TemplateView):
    template_name = 'room/home.html'