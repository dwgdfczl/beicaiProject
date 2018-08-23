# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BcprojectItem(scrapy.Item):
    标题 = scrapy.Field()
    
    预期年化利率 = scrapy.Field()
    
    投资期限 = scrapy.Field()
    
    收益方式 = scrapy.Field()
    
    投资金额 = scrapy.Field()
    
    预期收益 = scrapy.Field()
    
    操作 = scrapy.Field()
