from django.contrib import admin
from . models import Get_touch,CreateQuery, AboutUs



#custom Admin site start #
# admin.site.unregister(Group)
class Get_touchAdmin(admin.ModelAdmin):
  readonly_fields = ('name','email',)
  list_display = ('name', 'email', 'subject')
  list_filter = ('subject',)
  search_fields = ('name', 'email', 'subject')
#custom Admin site end #

# Register your models here.
admin.site.register(Get_touch, Get_touchAdmin)



#custom Admin site start #
class CreateQueryAdmin(admin.ModelAdmin):
  readonly_fields = ('name','email',)
  list_display = ('name', 'email', 'phone','created_at','department')
  list_filter = ('created_at','department')
  search_fields = ('name', 'email', 'department')
#custom Admin site end #

# Register your models here.
admin.site.register(CreateQuery, CreateQueryAdmin)

#custom Admin site start #

class AboutUsAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name', 'email')

admin.site.register(AboutUs, AboutUsAdmin)
#custom Admin site end #





