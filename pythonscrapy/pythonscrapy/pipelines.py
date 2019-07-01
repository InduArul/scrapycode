# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PythonscrapyPipeline(object):
    def process_item(self, item, spider):
            print ("pipeline:" + item['H1heading'][0])
            print ("pipeline:" + item['createdat'][0])
            print ("pipeline:" + item['parah'][0])
            return item
