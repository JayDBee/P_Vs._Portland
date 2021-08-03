from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def comingSoon(request):
    return render(request, 'comingSoon.html')