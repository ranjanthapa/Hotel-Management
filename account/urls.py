from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.SigInView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(next_page='room:home'), name="logout"),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.UserRegistrationView.as_view(), name="register"),

]
