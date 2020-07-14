from django import forms

from .models import Driver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('name', 'bio', 'avatar', 'car', 'contact')