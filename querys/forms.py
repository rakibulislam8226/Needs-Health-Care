from django import forms


class AnswerForm(forms.Form):
    answer_text =forms.CharField(widget=forms.Textarea)
 
    def __str__(self):
        return f"{self.answer_text}"


class SearchForm(forms.Form):
    title = forms.CharField(max_length=20)