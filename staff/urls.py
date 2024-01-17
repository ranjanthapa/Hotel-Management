from django.urls import path
from .views import staff_login, staff_dashboard, staff_logout

urlpatterns = [
    path('login/', staff_login, name='staff_login'),
    path('dashboard/', staff_dashboard, name='staff_dashboard'),
    path('logout/', staff_logout, name='staff_logout'),
    
]
