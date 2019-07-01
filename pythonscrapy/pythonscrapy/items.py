# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class pythonscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    URL = scrapy.Field()
    pagetitle = scrapy.Field()
    articlecreateddate = scrapy.Field()
    PageH1heading = scrapy.Field()
    Details = scrapy.Field()
    linkurls = scrapy.Field()

    
    