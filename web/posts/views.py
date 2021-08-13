from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))

from django.shortcuts import render
from django.http import HttpResponse
import random

from scripts.EveroutSpider import spider_runner_results

#below is not working 
#from scripts.results import spider_runner_results

#from EveroutSpider import EveroutSpider
#from TravelPDXSpider import TravelPortlandSpider


def home(request):
    #context = random.choice(spider_runner_results())
    return render(request, 'home.html')

#https://stackoverflow.com/questions/41495052/scrapy-reactor-not-restartable
def Events(request):
    context = random.choice(spider_runner_results())
    return render(request, 'EventPage.html', context)

def comingSoon(request):
    return render(request, 'comingSoon.html')
