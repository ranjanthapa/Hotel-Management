from django.urls import path
from . import views
app_name = 'room'

urlpatterns = [
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
    path('reservation/confirim/<str:uidb64>/<str:res_uidb64>', views.confirm_booking, name='room_confirmation'),
    path('roomdetail/<int:id>/', views.RoomDetailView.as_view(), name='roomdetail'),
]
