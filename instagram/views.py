from django.shortcuts import render
from django.http import HttpResponse
from . models import Image,tag
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm
# Create your views here.


@login_required(login_url='/accounts/register')
def welcome(request):
    images = Image.objects.all()
    return render(request,'index.html',{'images':images})

def home(request):
    return HttpResponse('lets ride fun with simple insta')  

def picture(request,image_id):
    picture = Image.objects.get(id = image_id)
    return render(request,'picture.html',{'picture':picture})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.UserProfile = current_user
            image.save()
    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})

