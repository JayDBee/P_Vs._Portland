#July 31. 21
#these will be the spiders used to collect information for the PVP application
import scrapy


#everout
class EveroutSpider(scrapy.Spider):
    #HenryEvery Aka
    name = "LongBen"
    allowed_domains = ["everout.com/portland/"]
    start_urls = (
        'https://everout.com/portland/events/the-big-one-pnw-rock-festival/e102790/',
        'https://everout.com/portland/events/feast-portland-presents-summer-of-feast/e101475/',
    )

    def parse(self, response):
        yield {
            "url": response.url,
            "title": response.css('h1::text').get(),
            "heading image": response.css('img ::attr(src)')[1].get(),
        }

       




#this code should be implemented next for dynamic intigration with django
#def __init__(self, *args, **kwargs):
        #self.url = kwargs.get('url')
        #self.domain = kwargs.get('domain')
        #self.start_urls = [self.url]
        #self.allowed_domains = [self.domain]

