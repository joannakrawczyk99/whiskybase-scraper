import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['whiskeybase.com']
    start_urls = ['http://whiskeybase.com/']

    def parse(self, response):
        pass
