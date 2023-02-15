from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import PatientSignUp, DoctorSignUp,User
from django.core.exceptions import ValidationError


class PatientSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    age=forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists. User another email to create an account.")
        return email

        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        name = self.cleaned_data['name']
        age = self.cleaned_data['age']
        phone = self.cleaned_data['phone']
        email = self.cleaned_data['email']
        patients = PatientSignUp.objects.create(user=user, name=name, age=age, phone=phone, email=email)
        patients.save()
        return user
    
    
class DoctorSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    age=forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.CharField(required=True)
    department = forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'phone', 'department', 'password1', 'password2']

 
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        # user.is_doctor = True     # need to approve from admin.
        user.save()
        name = self.cleaned_data['name']
        age = self.cleaned_data['age']
        phone = self.cleaned_data['phone']
        email = self.cleaned_data['email']
        department = self.cleaned_data['department']
        doctors = DoctorSignUp.objects.create(user=user, name=name, age=age, phone=phone, email=email, department=department)
        doctors.save()
        return user