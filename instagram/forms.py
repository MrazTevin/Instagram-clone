from .models import Image
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['userprofile', 'comments', 'tags', 'post']
        widget = {
            'tags':forms.CheckboxSelectMultiple(),
            }
