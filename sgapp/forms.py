from django import forms

from .models import Persons

class PersonsForm(forms.ModelForm):

    class Meta:
        model = Persons
        fields = ['first_name', 'last_name', 'email', 'phone', 'training']
        labels = {'first_name': 'Imię', 'last_name': 'Nazwisko', 'email': 'Adres e-mail', 'phone': 'Numer telefonu'}
        widgets = {'training': forms.HiddenInput()}