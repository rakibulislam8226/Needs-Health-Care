from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='payment_home'),
    path('donate/', views.DonateView, name='donate'),
    path('payment/success/', views.CheckoutSuccessView.as_view(), name='success'),
    path('payment/faild/', views.CheckoutFaildView.as_view(), name='faild'),
]


