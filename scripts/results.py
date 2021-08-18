#special thanks to this solution from:
#https://stackoverflow.com/questions/40237952/get-scrapy-crawler-output-results-in-script-file-function
#https://stackoverflow.com/questions/41495052/scrapy-reactor-not-restartable

from scrapy import signals
from scrapy.signalmanager import dispatcher
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from multiprocessing import Process, Queue
from EveroutSpider import EveroutSpider
from TravelPDXSpider import TravelPortlandSpider

import random


def spider_runner_results():
    #List of available spiders, one of which is randomly chosen
    list = [EveroutSpider, TravelPortlandSpider]
    Spider = random.choice(list)
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)
    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    runner = CrawlerRunner()
    d = runner.crawl(Spider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run() # the script will block here until the crawling is finished
    
    return results


if __name__ == '__main__':
    print(spider_runner_results())