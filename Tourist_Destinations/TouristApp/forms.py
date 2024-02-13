from django import forms
from .models import Destinations

class DestinationForms(forms.ModelForm):
    class Meta:
        model=Destinations
        fields='__all__'
        widgets = {
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'weather': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'map_link': forms.URLInput(attrs={'class': 'form-control'}),  # Adjusted field name to match the model
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }