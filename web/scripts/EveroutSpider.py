#July 31. 21
#these will be the spiders used to collect information for the PVP application
import scrapy
from scrapy import signals
from scrapy.signalmanager import dispatcher
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner


from multiprocessing import Process, Queue


#from EveroutSpider import EveroutSpider
#special thanks to this solution from:
#https://stackoverflow.com/questions/40237952/get-scrapy-crawler-output-results-in-script-file-function
#https://stackoverflow.com/questions/41495052/scrapy-reactor-not-restartable


#everout
class EveroutSpider(scrapy.Spider):
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
            "image": response.css('img ::attr(src)')[1].get(),
            "about": response.xpath("//div[@class='description']/text()").get().strip()
        }

def spider_runner_results():
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)
    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    runner = CrawlerRunner()
    d = runner.crawl(EveroutSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run() # the script will block here until the crawling is finished
    
    return results


if __name__ == '__main__':
    print(spider_runner_results())