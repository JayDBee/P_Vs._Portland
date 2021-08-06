from django.shortcuts import render
from django.http import HttpResponse

from random import choice
#from ..scripts.results import results

def home(request):
    return render(request, 'home.html')

def comingSoon(request):
    return render(request, 'comingSoon.html')

def comingSoon(request):
    #picks = spider_results()
    nums = [1,2,3,4,5]
    context = {"number": choice(nums)}
    return render(request, 'comingSoon.html', context)