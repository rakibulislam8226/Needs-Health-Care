from django.contrib import admin
from . models import *
# Register your models here.


#custom Admin site start #

class AmbulanceAdmin(admin.ModelAdmin):
  # readonly_fields = ('name','email',)
  list_display = ('driver_email','driver_name', 'driver_number', 'location')
  list_filter = ('location',)
  search_fields = ('location', 'driver_number', 'driver_name')
admin.site.register(Ambulance, AmbulanceAdmin)
#custom Admin site end #


#custom Admin site start #
class Ambulance_hireAdmin(admin.ModelAdmin):
  # readonly_fields = ('name','email',)
  list_display = ('name', 'number', 'location')
  list_filter = ('location',)
  search_fields = ('location', 'number', 'name')
admin.site.register(Ambulance_hire, Ambulance_hireAdmin)
#custom Admin site end #
