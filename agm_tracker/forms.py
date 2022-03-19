from django import forms
from .models import agm

class agmform(forms.ModelForm):
    class Meta:
        model = agm

        fields = ['codename',
                  'ticker',
                  'fund',
                  'position_name',
                  'agm_date',
                  'agm_record']