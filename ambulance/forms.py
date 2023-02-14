from django import forms
from . models import Ambulance, Ambulance_hire

class AmbulanceForm(forms.ModelForm):
  class Meta:
    model = Ambulance
    fields = '__all__'


class Ambulance_hireForm(forms.Form):
  number =forms.CharField(widget=forms.TextInput(attrs={'minlength': 11, 'maxlength': 14}))
  email =forms.EmailField(widget=forms.TextInput(attrs={'minlength': 11, 'maxlength': 14},), required=False)
  location =forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, 'placeholder': 'Thana, Road number, Home number, Area, Others info..'}))
  agree = forms.BooleanField(required=True)

  def __str__(self):
    return f"{self.number}"