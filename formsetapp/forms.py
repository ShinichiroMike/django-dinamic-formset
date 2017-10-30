from django import forms
from django.forms.formsets import BaseFormSet
from .models import Person

class PersonForm(forms.ModelForm):
  name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name',}), required=False)

  class Meta:
    model = Person
    fields = ('name',)