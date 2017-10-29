from django import forms
from django.forms.formsets import BaseFormSet

class PersonForm(forms.Form):
  name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name',}), required=False)