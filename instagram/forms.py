from .models import Image
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['userprofile', 'comments', 'tags', 'post']
        widget = {
            'tags':forms.CheckboxSelectMultiple(),
            }

class FileFieldForm(forms.Form):
    file_field = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))


