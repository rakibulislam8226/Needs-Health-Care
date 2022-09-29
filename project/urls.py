
from django.contrib import admin
from django.urls import path

from helper.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('shop/', shop,name='shop'),
    path('cart/', cart,name='cart'),
    path('checkout/', checkout,name='checkout'),
    path('departments/', departments,name='departments'),
    path('services/', services, name='services'),
    path('doctor/', doctor, name='doctor'),
]
