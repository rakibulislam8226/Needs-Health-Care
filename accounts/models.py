from django.db import models
from django.contrib.auth.models import User, AbstractUser



class User(AbstractUser):
    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    
    
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)  
    
    def __str__(self) -> str:
        return self.user.username 
    
    
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.user.username 
    
    