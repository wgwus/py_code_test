# -*- coding: utf-8 -*-
import scrapy


class UsersSpider(scrapy.Spider):
    name = 'users'
    allowed_domains = ['shiyanlou.com']
    def start_usls(self):
        
        start_urls = ['https://www.shiyanlou.com/users/{}/']
        return (url_tmp.format(i)) for i in range(525000, 524800, -10))

    def parse(self, response):

        for i in response.xpath('//div@[class='body']').extract():
            

            yield {
             'name':xpath('//div[@class="user-meta"]/span/text()').extract()[0].strip()
            # 'is_vip':xpath()extract_first().strip(),
             'status':xpath('//div[@class="user-status"]/span/text()').extract(default='w')[1].strip()
             'school_job'xpath('//div[@class="user-status"]/span/text()').extract()[0].strip()
             'level':xpath('//div[@class="user-meta"]/span/text()').extract()[1].strip()
             'join_date':xpath('//span[@class="user-join-date"]/text()').extract_first().strip() 
             'learn_history':xpath('//span[@class="tab-item"]/text()').extract_first(default='no').strip
            }