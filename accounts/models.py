from django.db import models
from django.contrib.auth.models import User, AbstractUser



class User(AbstractUser):
    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    
    
    
class DoctorSignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    hospital = models.CharField(max_length=110)
    education = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.user.username 
    
    class Meta:
        verbose_name_plural = "Doctors Accounts"
    
    
class PatientSignUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.user.username 
    
    class Meta:
        verbose_name_plural = "Patients Accounts"
    
    