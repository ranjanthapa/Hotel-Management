from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('rooms/', views.RoomListView.as_view(), name='rooms'),
    path('roomdetail/<int:id>/', views.RoomDetailView.as_view(), name='roomdetail'),
    path('bookroom/', views.RoomBookView.as_view(), name='bookroom'),
]
