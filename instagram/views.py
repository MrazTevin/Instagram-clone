from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . models import Image, tag, Profile
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.db import transaction
# from f import handle_uploaded_file
User = get_user_model

# Create your views here.

@login_required(login_url='/accounts/register')
def welcome(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})


def home(request):
    return HttpResponse('lets ride fun with simple insta')


def picture(request, image_id):
    picture = Image.objects.get(id=image_id)
    return render(request, 'picture.html', {'picture': picture})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.UserProfile = current_user
            image.save()
            return redirect('welcome')
    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})


def profile(request):
    user = Profile.objects.all()
    return render(request, 'profile.html', {"user": user})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def handle_uploaded_file(f):
    with open('media/photos', 'wb+')as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required
@transaction.atomic
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'lorem ipsum dollar sit amet'
    user.save()

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
