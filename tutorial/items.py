# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TutorialItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticleItem(Item):
    aid = Field()
    title = Field()
    body = Field()
    date = Field()
    nurl = Field()
    purl = Field()
    dfclass = Field()
    nclass = Field()
    nclass2 = Field()
    press = Field()
    num_comment = Field()