from django.urls import path
from . import views


urlpatterns = [
  path('home/', views.doctors_dashboard, name='doctor_dashboard'),
  path('unanswer-query/', views.unanswer_query_view, name='unanswer_query'),

]