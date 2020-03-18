import scrapy
import os

from scrapy.http import HtmlResponse


body = open('ex.html','r',encoding='utf-8').read()  #这里原来没有encoding 后加上去的 试了好多办法md


response = HtmlResponse(url='http://ex.com',body=body.encode('UTF-8'))
prin1 = response.xpath('/html/head/title').extract()  ###  / 节点

print2 = response.xpath('//h2/text()').extract()    ### 标签里的 文本
print3 = response.xpath('//img/@src').extract()    ### @ 选取一个属性
print4 = response.xpath('//p[@class="location"]/text()').extract()######用属性定位节点, class属性为location 的p 内的文本
print5 = response.xpath("//div[@class='companies']/div[2]").extract()   ###  div.companies 下的第二个div 子节点


print6 = response.xpath("//div[@class='companies']/div[2]").xpath('//a/@href').extract()
print7 =  response.xpath('//div[@class="companies"]/div[3]').xpath('.//a/@href').extract()
print8 = response.xpath('//div[contains(@class, "name2")]/text()').extract() 
 

num1 = 0
for i in (prin1,print2,print3,print4,print5,print6,print7,print8):
    num1 += 1
    print (num1)
    print (i)