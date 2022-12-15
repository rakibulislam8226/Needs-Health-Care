from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Patient, Doctor,User


class PatientSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    age=forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        name = self.cleaned_data['name']
        age = self.cleaned_data['age']
        patients = Patient.objects.create(user=user, name=name, age=age)
        patients.save()
        return user
    
    
class DoctorSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    age=forms.CharField(required=True)
    email = forms.CharField(max_length=255, required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        # user.is_doctor = True     # need to approve from admin.
        user.save()
        name = self.cleaned_data['name']
        age = self.cleaned_data['age']
        doctors = Doctor.objects.create(user=user, name=name, age=age)
        doctors.save()
        return user