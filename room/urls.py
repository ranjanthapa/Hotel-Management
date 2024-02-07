from django.urls import path
from . import views
app_name = 'room'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-us/', views.AboutUsView.as_view(), name='aboutus'),
    path('contact-us/', views.ContactUsView.as_view(), name='contactus'),
    path('events/', views.EventsView.as_view(), name='events'),
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
    path('rooms/', views.RoomListView.as_view(), name='rooms'),
    path('roomdetail/<int:id>/', views.RoomDetailView.as_view(), name='roomdetail'),
    path('bookroom/', views.RoomBookView.as_view(), name='bookroom'),
    # path('confirm/<uidb64>/<token>', views.confirm_booking, name='confirm_booking')
]
