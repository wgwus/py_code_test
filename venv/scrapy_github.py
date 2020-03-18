import scrapy


class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-courses'

    @property
    def start_urls(self):
        """ start_urls  需要返回一个可迭代对象，所以，你可以把它写成一个列表、元组或者生成器，这里用的是列表
        """
        url_list = ['https://github.com/shiyanlou?tab=repositories']
        return url_list

    def parse(self, response):
        for course in response.css('div.col-10'):
            yield 
            {
                'name': course.css('h3 a::text').extract_first().strip(),
                #'name': course.css('div.f6 relative-time::attr(datetime)').extract_first().strip(),
               
            }