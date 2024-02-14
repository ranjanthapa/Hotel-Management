from django.urls import path
from . import views
app_name = 'event'
urlpatterns = [
    path('', views.EventView.as_view(), name='events'),
    path('<slug:title>', views.EventDetailView.as_view(), name="event_detail"),

]
