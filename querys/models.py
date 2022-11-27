from django.db import models

# Create your models here.
class Query(models.Model):
  department = models.CharField(max_length=100, blank=True, default='')
  query = models.TextField(blank=True, default='')
  creator = models.ForeignKey('auth.User', related_name='user', on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['created_at']
  
  def __str__(self) -> str:
    return self.query[:50]


class Answer(models.Model):
  answer = models.TextField(blank=True, default='')
  creator = models.ForeignKey('auth.User', related_name='answer', on_delete=models.SET_NULL, null=True)
  query = models.ForeignKey(Query, related_name='answer', on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['created_at']
  
  def __str__(self) -> str:
    return self.answer[:50]