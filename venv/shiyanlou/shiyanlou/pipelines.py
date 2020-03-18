# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course,engine

class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        item['students']=int(item['students'])
        self.session.add(Course(**item))
        return item

    def open_spid(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_sipder(self, spider):
        self.session.commit()
        self.session.close()