import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    """ 
    使用 scrapy 爬取页面数据需要编写一个爬虫类，该爬虫类要继承 scrapy.Spider 类。在爬虫类中定义要请求的网站和链接、如何从返回的网页提取数据等等。
    在 scrapy 项目中可能会有多个爬虫，name 属性用于标识每个爬虫，各个爬虫类的 name 值不能相同
    """
    name = 'shiyanlou-courses'

    # 注意此方法的方法名字是固定的，不可更改
    def start_requests(self):
        """ 
        此方法需要返回一个可迭代对象，迭代的元素是 scrapy.Request 对象，可迭代对象可以是一个列表或者迭代器，这样 scrapy 就知道有哪些网页需要爬取了。scrapy.Request 接受一个 url 参数和一个 callback 参数：url 指明要爬取的网页；callback 是一个回调函数，用于处理返回的网页，它的值通常是一个提取数据的 parse 方法。
        """

    # 注意此方法的方法名字也是固定的，不可更改
    def parse(self, response):
        """ 
        这个方法作为 scrapy.Request 的 callback ，在里面编写提取数据的代码。scrapy 中的下载器会下载 start_reqeusts 中定义的每个 Request 并且将结果封装为一个 response 对象传入这个方法。
        """
        for course in response.css('div.col-md-3'):
            yield{
                'name' :course.css('h6.course-name::text').extract_first().strip(),
                'description': course.css('div.course-description::text').extract_first().strip(),
                #'type': course.css('span.course-list-tag::text').extract_first().strip(),


                'students': course.css('span.students-count span::text').extract_first()

            } 


    def start_requests(self):
        # 课程列表页面 URL ，注意此列表中的地址可能有变动，需手动打开页面复制最新地址
        url_list = ['https://www.shiyanlou.com/courses/',
                    'https://www.shiyanlou.com/courses/?page_size=20&cursor=bz0yMA%3D%3D',
                    'https://www.shiyanlou.com/courses/?page_size=20&cursor=bz00MA%3D%3D']
        # 返回一个生成器，生成 Request 对象，生成器是可迭代对象
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse)

