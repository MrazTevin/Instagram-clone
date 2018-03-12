from django.shortcuts import render
from django.http import HttpResponse
from . models import Image,tag
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/accounts/login')
def welcome(request):
    images = Image.objects.all()
    return render(request,'index.html',{'images':images})

def home(request):
    return HttpResponse('lets ride fun with simple insta')  

def picture(request,image_id):
    picture = Image.objects.get(id = image_id)
    return render(request,'picture.html',{'picture':picture})