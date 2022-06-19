import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor 
from w3lib.html import remove_tags
from core1.items import Core1Item


class Singlider(scrapy.Spider):
    name = 'czone'
    
    start_urls = ['https://www.czone.com.pk/laptops-pakistan-ppt.74.aspx']
    
    def parse(self, response):
        links = response.css('li ul.dropdown-menu li.megamenu-content ul')
        for l in links:
            for i in l.css('ul li.child'):
                yield response.follow(i.css('li a::attr(href)').get().replace('/', 'https://www.czone.com.pk/'), callback=self.parse_items)
                    
    def parse_items(self, response):
        item = Core1Item()
        for instance in response.xpath('//*[@id="divListView"]/div[@class="template"]'):
            item['name'] = instance.css('div.product > div > div > div > div > h4 > a::text').get()
            item['image'] = 'https://www.czone.com.pk' + instance.css('div.product > div > div > div.image > a > img').attrib['src']
            item['detail'] = instance.css('div.product > div > div > div > div > div > p::text').get()
            item['specs'] = remove_tags(instance.css('div.product > div > div > div > div > ul').get())
            item['availability'] = instance.css('div.product > div > div > div > div > div[class=product-stock] > span + span::text').get()
            item['price'] = instance.css('div.product > div > div > div > div > div[name=list-price] > span::text').get()
            
            yield item
        next_page = response.css('div > div > ul > li > a#anNextPage::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_items)








