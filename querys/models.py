from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=20)
    post = models.TextField()
 
    def __str__(self):
        return f"Post: {self.post_title}"
 
class AnswerPost(models.Model):
    name = models.CharField(max_length=20)
    answer_text = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
     
    def __str__(self):
        return f"Answer by Name: {self.name}"
    
    class Meta:
      ordering = ['-id']

# class Query(models.Model):
#   department = models.CharField(max_length=100, blank=True, default='')
#   query = models.TextField(blank=True, default='')
#   creator = models.ForeignKey('accounts.User', related_name='user', on_delete=models.SET_NULL, null=True)
#   created_at = models.DateTimeField(auto_now_add=True)

#   class Meta:
#     ordering = ['created_at']
  
#   def __str__(self) -> str:
#     return self.query[:50]


# class Answer(models.Model):
#   answer = models.TextField(blank=True, default='')
#   creator = models.ForeignKey('accounts.User', related_name='answer', on_delete=models.SET_NULL, null=True)
#   query = models.ForeignKey(Query, related_name='answer', on_delete=models.SET_NULL, null=True)
#   created_at = models.DateTimeField(auto_now_add=True)

#   class Meta:
#     ordering = ['created_at']
  
#   def __str__(self) -> str:
#     return self.answer[:50]