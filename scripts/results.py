#imports signals for when events occur
from scrapy import signals
#functionality of start() and stop()
from scrapy.crawler import CrawlerProcess
#import project settings
from scrapy.utils.project import get_project_settings
#connects receivers to signals
from scrapy.signalmanager import dispatcher

from EveroutSpider import EveroutSpider
#special thanks to this solution from:
#https://stackoverflow.com/questions/40237952/get-scrapy-crawler-output-results-in-script-file-function

def spider_results():
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(EveroutSpider)
    process.start()  # the script will block here until the crawling is finished
    return results


#prints lists which contain dictionaries with scrapy results
if __name__ == '__main__':
    print(spider_results())