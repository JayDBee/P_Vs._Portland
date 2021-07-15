#import requests
from bs4 import BeautifulSoup
import asyncio
from pyppeteer import launch
#import os

URL = "https://www.portlandmercury.com/blogtown/2021/07/13/35028680/most-heatwave-victims-died-alone-with-no-air-conditioning-county-report-finds"

async def main():
    browser = await launch()
    page = await browser.newPage()

    await page.goto(URL)
    page_content = await page.content()

    #soup
    soup = BeautifulSoup(page_content, "html.parser")
    results = soup.find(class_="article-text category-blogtown")
    print(results.prettify())
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

#should only print pg. txt for confirmation
#print(page.text)
#print(page.content



#in page, search for 
#Entire article @ <div id="articleComponent-#####" class="component">
#Headline @ <h1 class="headline">...</h1>
#IMG @ <div class="blogImageCenter img-responsive" style>...</div>
#Text @ <div class = "article-text category-blogtown">

#now that we have the page source, get the article txt
#print txt

#save the text
#END





#const int LIMIT;
#FRESHNESS
#if data has been "LIVE" for longer than LIMIT, then take off
#should always be "running"