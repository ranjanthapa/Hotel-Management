from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutUsView.as_view(), name='about'),
    path('contact/', views.ContactUsView.as_view(), name='contact'),
    path('rooms/', views.RoomListView.as_view(), name='rooms'),
]
