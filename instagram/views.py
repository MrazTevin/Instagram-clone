from django.shortcuts import render
from django.http import HttpResponse
from . models import Image,tag
# Create your views here.

def welcome(request):
    images = Image.objects.all()
    return render(request,'index.html',{'images':images})

def home(request):
    return HttpResponse('lets ride fun with simple insta')  