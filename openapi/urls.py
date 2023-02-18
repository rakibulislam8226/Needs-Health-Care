from django.urls import path
from . import views

# a list of all the urls
urlpatterns = [
    path('home/', views.home, name='chatapt'),
    path('error-handler/', views.error_handler, name='error_handler'),
]