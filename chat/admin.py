from django.contrib import admin
from .models import Room, Message

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name', )
  list_per_page = 20
admin.site.register(Room, RoomAdmin)

class MessageAdmin(admin.ModelAdmin):
  list_display = ('short_value', 'room','user','get_date')
  search_fields = ('date','room','user')
  list_per_page = 20
admin.site.register(Message, MessageAdmin)
