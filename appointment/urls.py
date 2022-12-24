from django.urls import path
from . views import *

urlpatterns = [
    path('appointment/add/', create_view, name='add_appointment'),
    path('appointment/ajax/load-doctors/', load_doctors, name='ajax_load_doctors'),
]
