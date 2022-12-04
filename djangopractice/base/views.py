from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request): #example funtion
    return HttpResponse('Home pages') #example function

def room(request): #Example
    return HttpResponse('ROOM') #Example