from django import forms
from .models import GeeksModel


class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text="enter 6 digit number")
    password = forms.CharField(widget=forms.PasswordInput())


class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = '__all__'
