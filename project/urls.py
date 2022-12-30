
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

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
    path('', home,name='home'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('accounts.urls')),
    path('find-doctor/', include('find_doctors.urls')),
    path('query/', include('querys.urls')),
    path('appointment/', include('appointment.urls')),
    path('', include('ambulance.urls')),
    path('', include('chat.urls')),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    
   #  path('ambulance-list/', AmbulanceList.as_view(), name='ambulance'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header  =  "Needs Healthcare admin"  
admin.site.site_title  =  "Needs Healthcare admin site"
admin.site.index_title  =  "Needs Healthcare Admin"