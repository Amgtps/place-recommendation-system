import scrapy


class HolidifycrawlerSpider(scrapy.Spider):
    name = 'HolidifyCrawler'
    allowed_domains = ['www.holidify.com']
    start_urls = ['http://www.holidify.com/']

    def parse(self, response):
        pass
