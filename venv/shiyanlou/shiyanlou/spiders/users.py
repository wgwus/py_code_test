# -*- coding: utf-8 -*-
import scrapy
from ..items import UserItem

class UsersSpider(scrapy.Spider):
    name = 'users'
    allowed_domains = ['shiyanlou.com']
    def start_usls(self):
        
        start_urls = 'https://www.shiyanlou.com/users/{}/'
        return (start_urls.format(i) for i in range(525000, 524800, -10))

    def parse(self, response):

        #for i in respose.xpath('//div@[class="body"]').extract():
            

        item = UserItem(
            name = response.xpath('//div[@class="user-meta"]/span/text()').extract()[0].strip(),
        # 'is_vip':xpath()extract_first().strip(),
            status = response.xpath('//div[@class="user-status"]/span/text()').extract(default='w')[1].strip(),
            school_job = response.xpath('//div[@class="user-status"]/span/text()').extract()[0].strip(),
            level = response.xpath('//div[@class="user-meta"]/span/text()').extract()[1].strip(),
            join_date = response.xpath('//span[@class="user-join-date"]/text()').extract_first().strip(), 
            learn_courses_sum = response.xpath('//span[@class="tab-item"]/text()').extract_first(default='no').strip()
        )
        if len(response.css('div.user-avatar img').extract()) == 2:
            item['is_vip'] = True

        return item
