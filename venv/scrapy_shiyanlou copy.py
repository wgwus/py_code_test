import scrapy


class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-courses'

    @property
    def start_urls(self):
        """ start_urls  需要返回一个可迭代对象，所以，你可以把它写成一个列表、元组或者生成器，这里用的是列表
        """
        url_list = ['https://www.shiyanlou.com/courses/',
                    'https://www.shiyanlou.com/courses/?page_size=20&cursor=bz0yMA%3D%3D',
                    'https://www.shiyanlou.com/courses/?page_size=20&cursor=bz00MA%3D%3D']
        return url_list

    def parse(self, response):
        for course in response.css('div.col-md-3'):
            yield {
                'name': course.css('h6::text').extract_first().strip(),
                'description': course.css('div.course-description::text').extract_first().strip(),
                'type': course.css('span.course-type::text').extract_first().strip(),
                'students': course.css('span.students-count span::text').extract_first()
            }