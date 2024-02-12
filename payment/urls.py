from django.urls import path
from . import views


app_name = 'payment'
urlpatterns = [
    path('', views.PaymentView.as_view(), name='pay'),
    path('create-checkout-session/', views.CreateSessionCheckOutView.as_view(), name='create-checkout-session'),
    path('config/', views.stripe_config, name='config')
]
