from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return render(request,'index.html')

def home(request):
    return HttpResponse('lets ride fun with simple insta')