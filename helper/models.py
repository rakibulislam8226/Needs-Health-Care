from django.db import models


# Create your models here.
class Get_touch(models.Model):
  name=models.CharField(max_length=50)
  email=models.EmailField(max_length=50)
  subject=models.CharField(max_length=300)
  message=models.TextField()
  def __str__(self):
    return self.name + " - "+ self.email

class CreateQuery(models.Model):
  DEPARTMENT = (
  ('CARDIOLOGY', 'CARDIOLOGY'),
  ('NEUROLOGY', 'NEUROLOGY'),
  ('ORTHOPEDICS', 'ORTHOPEDICS'),
  ('CANCER DEPARTMENT', 'CANCER DEPARTMENT'),
  ('OPHTHALMOLOGY', 'OPHTHALMOLOGY'),
  ('RESPIRATORY', 'RESPIRATORY'),
  )
  name=models.CharField(max_length=50)
  phone=models.CharField(max_length=50)
  email=models.EmailField(max_length=50)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  department=models.CharField(max_length=21, choices=DEPARTMENT)
  describe=models.TextField()
  def __str__(self):
    return self.name + " - "+ self.department
  


