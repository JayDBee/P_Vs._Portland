from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
import scrapy

from twisted.internet import reactor


from EveroutSpider import EveroutSpider
#special thanks to this solution from:
#https://stackoverflow.com/questions/40237952/get-scrapy-crawler-output-results-in-script-file-function

def spider_runner_results():
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    runner = CrawlerRunner()
    d = runner.crawl(EveroutSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run() # the script will block here until the crawling is finished
    
    return results[0]


#our paramaeters can include the spider to use
def spider_results():
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(EveroutSpider)
    process.start()  # the script will block here until the crawling is finished
    return results[0]


#prints lists which contain dictionaries with scrapy results
if __name__ == '__main__':
    print(spider_runner_results())
    print("\n\n\n")
    #print(spider_results())
    