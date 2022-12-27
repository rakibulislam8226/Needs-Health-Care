from django.urls import path
from . import views

urlpatterns = [
    path('ambulances/', views.ambulance_list, name='ambulance_list'),

    path('create-ambulance/', views.create_ambulance, name='create_ambulance'),

    path('ambulance/<int:_id>/', views.ambulance_detail_view, name='ambulance_detail_view'),

]




