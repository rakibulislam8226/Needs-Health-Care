from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['post_title','post']


class AnswerForm(forms.Form):
    answer_text =forms.CharField(widget=forms.Textarea)
 
    def __str__(self):
        return f"{self.answer_text}"


class SearchForm(forms.Form):
    title = forms.CharField(max_length=20)