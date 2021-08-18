from bs4 import BeautifulSoup
import asyncio
from pyppeteer import launch

#command line array passed?


URL = "https://everout.com/portland/events/live-at-the-lot-liv-warfield-presented-by-portland-radio-project/e102492/"

#Format of this code is found in the link below:
#https://scrapingant.com/blog/scrape-dynamic-website-with-python

async def main():
    #launch browser
    browser = await launch()
    page = await browser.newPage()

    await page.goto(URL)
    page_content = await page.content()

    #soup
    soup = BeautifulSoup(page_content, "html.parser")
    results = soup.find(class_ = 'description')

    #display
    print(results.get_text())

    #close ends
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())