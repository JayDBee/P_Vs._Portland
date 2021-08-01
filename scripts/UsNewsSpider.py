#July 31. 21
#these will be the spiders used to collect information for the PVP application
import scrapy


#usnews
class UsNewsSpider(scrapy.Spider):
    #Sir Henry
    name = "Morgan"
    allowed_domains = ['travel.usnews.com/Portland_OR/Things_To_Do/']
    start_urls = (
        "https://travel.usnews.com/Portland_OR/Things_To_Do/Washington_Park_21334/"
    )

    def parse(self, response):
        yield {

        }
