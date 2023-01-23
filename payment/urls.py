from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='payment_home'),
    path('donate/', views.DonateView, name='donate'),
    path('success/', views.CheckoutSuccessView.as_view(), name='success'),
    path('faild/', views.CheckoutFaildView.as_view(), name='faild'),
    path('success/render/appointment/', TemplateView.as_view(template_name="payment/render_appointment.html")),
]


