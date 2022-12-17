from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  path('post-create/', views.PostCreateView, name='postcreate'),
  path('search/', views.SearchResultView.as_view(), name='search'),
  path('posts/', views.PostListView, name='posts'),
  path('post/<int:_id>', views.PostDetailView, name='post'),
    
  # path('querys/', views.QueryList.as_view()),
  # path('querys/<int:pk>/', views.QueryDetail.as_view()),
  # path('answer/', views.AnswerList.as_view()),
  # path('answer/<int:pk>/', views.AnswerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)