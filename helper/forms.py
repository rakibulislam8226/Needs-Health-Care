from django import forms
from . models import CreateQuery

class CreateQueryForm(forms.ModelForm):
  class Meta:
    model=CreateQuery
    fields = "__all__"
    