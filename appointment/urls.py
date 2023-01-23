from django.urls import path
from . views import *

urlpatterns = [
    path('add/', create_view, name='add_appointment'),
    path('appointment/ajax/load-doctors/', load_doctors, name='ajax_load_doctors'),

    path('total_appointments/', total_appointments, name='total_appointments'),
    path('user_appointments/<int:_id>/', user_appointments, name='user_appointments'),

    path("prescription_pdf/<int:_id>/", prescription_pdf, name="prescription_pdf"),
    
    path("my_appointments/", my_appointments, name="my_appointments"),
]
