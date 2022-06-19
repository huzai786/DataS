# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Core1Item(scrapy.Item):
    name = scrapy.Field()
    image = scrapy.Field()
    detail = scrapy.Field()
    specs  = scrapy.Field()
    availability = scrapy.Field()
    price = scrapy.Field()
    
