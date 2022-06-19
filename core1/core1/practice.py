import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse, Request
from w3lib.html import remove_tags


data = ''

with open('ex.html', 'r') as f:
    data += f.read()


res = HtmlResponse('',body=data , encoding='utf-8')

s = Selector(res)
links = s.css('li ul.dropdown-menu li.megamenu-content ul')
for l in links:
    for i in l.css('ul li.child'):
        print(i.css('li a::attr(href)').get().replace('/', 'https://www.czone.com.pk/'))
