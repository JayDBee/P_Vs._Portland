import requests
from selenium import webdriver
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)


#const int LIMIT;
#FRESHNESS
#if data has been "LIVE" for longer than LIMIT, then take off
#should always be "running"