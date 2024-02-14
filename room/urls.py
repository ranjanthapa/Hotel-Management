from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-us/', views.AboutUsView.as_view(), name='aboutus'),
    path('contact-us/', views.ContactUsView.as_view(), name='contactus'),
    path('events/', views.EventsView.as_view(), name='events'),
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
    path('rooms/', views.RoomListView.as_view(), name='rooms'),
    path('rooms/<str:room_type>/', views.RoomListView.as_view(), name='rooms_by_type'),
    path('room/detail/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    path('bookroom/', views.RoomBookView.as_view(), name='bookroom'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
