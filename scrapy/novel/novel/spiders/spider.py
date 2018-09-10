import scrapy
from novel.items import NovelItem
class DaomuSpider(scrapy.Spider):
    name = 'daomubiji'
    allowed_domains=['daomubiji.com']
    start_urls = ['http://www.daomubiji.com']
    def start_requests(self):
        urls = self.start_urls
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parseUrl)
    def parseUrl(self,response):
        for item in response.xpath('//ul/li'):
            if len(item.xpath('a/@href').extract()):
                url = item.xpath('a/@href').extract()[0]
                yield scrapy.Request(url=url,meta={'title_name':item.xpath('a/text()').extract()[0]},callback=self.parsePart)
            
    def parsePart(self,response):
        items = response.xpath('//article')
        # title = DaomuItem()
        filename = response.meta['title_name']
        for item in items:
            title = item.xpath('a/text()').extract()
            if len(title):
                with open(filename+'.txt','a') as f:
                    f.write(title[0]+'\n')
        # print("下载完成！")
