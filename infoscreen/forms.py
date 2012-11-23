from django import forms
from .models import InfoBox

class InfoBoxForm(forms.ModelForm):
    class Meta:
        model = InfoBox
