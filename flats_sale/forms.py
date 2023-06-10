from django import forms

class FlatSearchForm(forms.Form):
    search = forms.CharField(max_length = 128)
