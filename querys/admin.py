from django.contrib import admin
from . models import Query, Answer
# Register your models here.

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
  list_display = ('creator','department','created_at')
  # search_fields = ('name','department')
  list_filter = ('department',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
  list_display = ('creator','created_at','query')
  # search_fields = ('name','department')
