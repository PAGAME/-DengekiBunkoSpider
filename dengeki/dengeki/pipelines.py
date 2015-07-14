# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class DengekiPipeline(object):

    def __init__(self):
        self.file_obj = open('content', 'w')
        self.dict = {

        }

    def process_item(self, item, spider):
        json_content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file_obj.write(json_content)
        self.file_obj.close()
        return item
