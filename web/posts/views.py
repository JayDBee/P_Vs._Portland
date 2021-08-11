from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))

from django.shortcuts import render
from django.http import HttpResponse
import random

from scripts.EveroutSpider import spider_runner_results, run_spider


def home(request):
    return render(request, 'home.html')

def comingSoon(request):
    return render(request, 'comingSoon.html')

def comingSoon(request):
    #context = random.choice(run_spider())
    context = random.choice(spider_runner_results())
    return render(request, 'comingSoon.html', context)

#https://stackoverflow.com/questions/41495052/scrapy-reactor-not-restartable