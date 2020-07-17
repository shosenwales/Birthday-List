from django import forms
from django.forms import ModelForm

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class BirthdaysForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Add Birthday...'}))
    class Meta:
        model = Birthdays
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }