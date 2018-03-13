from .models import Image
from django.forms import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        widget = {
            'tags':forms.CheckboxSelectMultiple(),
            }
