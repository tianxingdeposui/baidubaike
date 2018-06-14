# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidubaikeItem(scrapy.Item):
    # define the fields for your item here like:
    #词条名字
    name = scrapy.Field()
    #词条内容
    content = scrapy.Field()
    #词条简介
    summary = scrapy.Field()
    #词条地址url
    url = scrapy.Field()
    #词条基本属性
    basicinfo = scrapy.Field()
    #词条明星关系
    starrelationlist = scrapy.Field()
    #词条标签
    tags = scrapy.Field()
    #编辑次数
    editCount = scrapy.Field()
    #分享次数
    shareCount = scrapy.Field()
    #喜欢次数
    likeCount = scrapy.Field()
    #pvurl
    pvurl = scrapy.Field()
    #总浏览量
    pv = scrapy.Field()
    #词条源码
    # html = scrapy.Field()