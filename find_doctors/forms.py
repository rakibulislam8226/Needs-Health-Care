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