from django.urls import path
from . import views


urlpatterns = [
  path('patient/add/', views.create_view, name='add'),
  path('patient/ajax/load-doctors/', views.load_doctors, name='ajax_load_doctors'),

]