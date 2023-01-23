from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='payment_home'),
    path('donate/', views.DonateView, name='donate'),
    path('success/', views.CheckoutSuccessView.as_view(), name='success'),
    path('faild/', views.CheckoutFaildView.as_view(), name='faild'),
]


