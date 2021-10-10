from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('страница приложения women')

def categories(request):
    return HttpResponse('<h1>The page with categories</h1>')
# Create your views here.
