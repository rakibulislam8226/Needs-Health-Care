from django.db import models


# Create your models here.
class Department(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name


class Doctor(models.Model):
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name


class Patients(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField(max_length=255)
  phone = models.CharField(max_length=15)
  department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
  doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.name