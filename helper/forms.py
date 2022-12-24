from django import forms
from . models import CreateQuery, Ambulance

class CreateQueryForm(forms.ModelForm):
  class Meta:
    model=CreateQuery
    fields = "__all__"
    
class AmbulanceForm(forms.ModelForm):
  class Meta:
    model=Ambulance
    fields = "__all__"