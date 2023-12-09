# forms.py

from django import forms
from .models import Item, Location

class ItemForm(forms.ModelForm):
    # Use ModelChoiceField for the location field
    location = forms.ModelChoiceField(queryset=Location.objects.all())

    widgets = {
        'court_date': forms.DateInput(attrs={'type': 'date'}),
    }

    class Meta:
        model = Item
        fields = ['description', 'location', 'disposition', 'digital_media', 'court_date', 'barcode']
        exclude = ['user', 'barcode']  # Exclude the user and barcode fields from the form
