from .models import Image, User, Profile
from django import forms


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['userprofile', 'comments', 'tags', 'post']
        widget = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

# class CommentsForm(forms.ModelForm):
#     class Meta:
#         model = comment

class UserForm(forms.ModelForm):
    model = User
    fields = {'first_name','last_name','email'}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo')

