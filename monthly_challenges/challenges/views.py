from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jan(request):
    return  HttpResponse("let's go to work")

def feb(request):
    return  HttpResponse("do swim")