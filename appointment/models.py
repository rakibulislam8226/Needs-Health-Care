from django.db import models
import datetime
from multiselectfield import MultiSelectField
from ambulance.models import PossiblePhoneNumberField


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Patients(models.Model):
    SEX = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    age = models.PositiveSmallIntegerField()
    sex = models.CharField(choices=SEX, default='Male', max_length=6, )
    email = models.EmailField(max_length=255)
    phone = PossiblePhoneNumberField(blank=True, default="")
    describe_your_problems = models.TextField()
    report = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.email
    
    class Meta:
      verbose_name = "Appointment"


class PatientAppointmentAnswer(models.Model):
    CHOICES = (
        ('Before Breakfast', 'Before Breakfast'),
        ('After Breakfast', 'After Breakfast'),
        ('Before Lunch', 'Before Lunch'),
        ('After Lunch', 'After Lunch'),
        ('Before Dinner', 'Before Dinner'),
        ('After Dinner', 'After Dinner'),
    )

    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    test = models.CharField(max_length=255, null=True, blank=True)
    medicine_one = models.CharField(max_length=255, null=True, blank=True)
    medicine_two = models.CharField(max_length=255, null=True, blank=True)
    medicine_three = models.CharField(max_length=255, null=True, blank=True)
    medicine_others = models.CharField(max_length=500, null=True, blank=True)
    advice = models.TextField(null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    medicine_eating_time = MultiSelectField(choices=CHOICES, max_choices=3, max_length=200)

    def __str__(self):
        return self.patient.email

    class Meta:
      verbose_name = "Patient Appointment Answer"
