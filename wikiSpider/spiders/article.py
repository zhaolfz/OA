import scrapy
import requests

class ArticleSpider(scrapy.Spider):
    name = 'article'

    def start_requests(self):

        urls = ['https://tieba.baidu.com/',
                'https://movie.douban.com/chart',
                'https://en.wikipedia.org/wiki/Python_%28programming_language%29']
        return [scrapy.Request(url=url,callback=self.parse) for url in urls ]

    def parse(self, response):
        url = response.url
        title = response.xpath("//h1/text()").extract_first()
        print('url is:{}'.format(url))
        print('title is:{}'.format(title))
