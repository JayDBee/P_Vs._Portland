#July 31. 21
#these will be the spiders used to collect information for the PVP application
import scrapy


#travelportland
class TravelPortlandSpider(scrapy.Spider):
    #William
    name = "Kidd"
    allowed_domains = ["travelportland.com/attractions/"]
    start_urls = (

        #commented don't work, try parsing by if there is an article heading/ xpath for main content
        

        #'https://www.travelportland.com/attractions/portland-saturday-market/',
        'https://www.travelportland.com/attractions/forest-park/',
        #'https://www.travelportland.com/attractions/powells/',
        'https://www.travelportland.com/attractions/portland-rose-garden/',
    )

    def parse(self, response):

        imgList = response.css('img::attr(src)').getall()
        firstjpg = [i for i in imgList if 'jpg' in i]

        yield {
            "url": response.url,
            "title": response.css('h1::text').get(),
            "heading image": firstjpg[0],
        }
