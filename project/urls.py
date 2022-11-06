
from django.contrib import admin
from django.urls import path,include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Needs Automatic Prescription API",
      default_version='v1',
      description="Automatic Prescription description",
      terms_of_service="https://www.needs.com/policies/terms/",
      contact=openapi.Contact(email="needs@mail.com"),
      license=openapi.License(name="Needs License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

from helper.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('', home,name='home'),
    path('shop/', shop,name='shop'),
    path('cart/', cart,name='cart'),
    path('checkout/', checkout,name='checkout'),
    path('departments/', departments,name='departments'),
    path('services/', services, name='services'),
    path('doctor/', doctor, name='doctor'),
    path('ambulance/', ambulance, name='ambulance'),
]
