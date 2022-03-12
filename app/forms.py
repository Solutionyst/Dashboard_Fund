from django import forms
from .models import position

class PositionForm(forms.ModelForm):
    class Meta:
        model = position

        fields = ['ticker',
                  'company_name',
                  'country',
                  'indice']