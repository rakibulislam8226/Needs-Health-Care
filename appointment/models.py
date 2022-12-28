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
  user=models.ForeignKey("accounts.User",on_delete=models.CASCADE)
  department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
  doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=30)
  email = models.EmailField(max_length=255)
  phone = models.CharField(max_length=15)
  describe_your_problems = models.TextField()

  def __str__(self):
    return self.name


class PatientAppointmentAnswer(models.Model):
  patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
  test = models.CharField(max_length=255, null=True, blank=True)
  medicine_one = models.CharField(max_length=255, null=True, blank=True)
  medicine_two = models.CharField(max_length=255, null=True, blank=True)
  medicine_three = models.CharField(max_length=255, null=True, blank=True)
  medicine_others = models.CharField(max_length=500, null=True, blank=True)
  advice = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.patient.name