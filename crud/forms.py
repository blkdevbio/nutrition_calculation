from django import forms
from .models import Menu

class CreateForm(forms.Form):
    menu = forms.CharField(label='menu')
    calorie = forms.FloatField(label='calorie')
    date = forms.DateField(label='date',widget=forms.DateInput(attrs={"type": "date"}),)