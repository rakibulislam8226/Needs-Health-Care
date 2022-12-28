from django import forms
from .models import Patients, Doctor


class PatientForm(forms.ModelForm):
  class Meta:
    model = Patients
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['doctor'].queryset = Doctor.objects.none()

    if 'department' in self.data:
      try:
        department_id = int(self.data.get('department'))
        self.fields['doctor'].queryset = Doctor.objects.filter(department_id=department_id).order_by('name')
      except (ValueError, TypeError):
        pass  # invalid input from the client; ignore and fallback to empty City queryset
    elif self.instance.pk:
      self.fields['doctor'].queryset = self.instance.department.doctor_set.order_by('name')

  
class PatientAppointmentAnswerForm(forms.Form):
  test =forms.CharField(widget=forms.TextInput(attrs={'minlength': 11, 'maxlength': 14}))
  medicine_one =forms.CharField(widget=forms.TextInput(attrs={'minlength': 11, 'maxlength': 14}))
  medicine_two =forms.CharField(widget=forms.TextInput(attrs={'minlength': 11, 'maxlength': 14}))
  medicine_three =forms.CharField(widget=forms.TextInput(attrs={'minlength': 11, 'maxlength': 14}))
  medicine_others =forms.CharField(widget=forms.TextInput(attrs={'minlength': 11, 'maxlength': 14}))
  advice =forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, 'placeholder': 'Thana, Road number, Home number, Area, Others info..'}))

  def __str__(self):
    return f"{self.medicine_one}"