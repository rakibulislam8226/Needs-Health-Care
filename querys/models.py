from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=255)
    descriptions = models.TextField()
    # answer_post = models.ForeignKey('AnswerPost', on_delete=models.CASCADE, null=True, blank=True, related_name='answer')

    class Meta:
        ordering = ['-id']
 
    def __str__(self):
        return f"Post: {self.post_title}"


    # @property
    # def get_answere_list(self):
    #     return self.answere_list_set.all()



 
class AnswerPost(models.Model):
    name = models.CharField(max_length=20)
    answer_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
     
    def __str__(self):
        return f"Answer by Name: {self.name} test {self.answer_text}"
    
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