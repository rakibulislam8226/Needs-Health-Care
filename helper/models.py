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
  date=models.DateField()
  department=models.CharField(max_length=20, choices=DEPARTMENT)
  describe=models.TextField()