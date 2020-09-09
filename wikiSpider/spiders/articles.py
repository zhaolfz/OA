import scrapy
from scrapy.contrib.spider import
from scrapy.contrib.link

class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
