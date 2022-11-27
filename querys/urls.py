from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  path('querys/', views.QueryList.as_view()),
  path('querys/<int:pk>/', views.QueryDetail.as_view()),
  path('answer/', views.AnswerList.as_view()),
  path('answer/<int:pk>/', views.AnswerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)