from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from . import models
from . import serializers

# Create your views here.
class QueryList(generics.ListCreateAPIView):
  queryset = models.Query.objects.all()
  serializer_class = serializers.QuerySerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(creator=self.request.user)

class QueryDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Query.objects.all()
  serializer_class = serializers.QuerySerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]



class AnswerList(generics.ListCreateAPIView):
  queryset = models.Answer.objects.all()
  serializer_class = serializers.AnswerSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(creator=self.request.user)

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Answer.objects.all()
  serializer_class = serializers.AnswerSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]