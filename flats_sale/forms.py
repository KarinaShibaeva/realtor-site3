from django import forms
from django.utils.translation import ugettext_lazy as _

class FlatSearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield", 'placeholder': 'Поиск'}), label=_(u'Имя'))
