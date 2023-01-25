from django.urls import path
from . import views


urlpatterns = [
  path('home/', views.doctors_dashboard, name='doctor_dashboard'),
  path('query_view/<int:_id>/', views.query_view, name='query_view'),

]