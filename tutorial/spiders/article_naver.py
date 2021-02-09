# -*- coding: utf-8 -*-

import os
import scrapy
import csv
from scrapy.selector import Selector
from scrapy.http.request import Request
from tutorial.items import ArticleItem


class ArticleNaverSpider(scrapy.Spider):
    name = 'article_naver'
    allowed_domains = ['news.naver.com']
    start_urls = []

    try:
        with open(os.getcwd()+"/naver.csv") as c_file:
            reader = csv.DictReader(c_file)
            for row in reader:
                start_urls += [row['url']]
    except IOError as err:
        print("File error:" + str(err))

    # nurl, press, title, date
    def parse(self, response):
        sel = Selector(response)
        nurl1s = sel.xpath('//ul[@class="type06_headline"]')
        nurl2s = response.xpath('//ul[@class="type06"]')

        for nurl1 in nurl1s:
            url1 = nurl1.xpath('li/dl/dt[@class="photo"]/a/@href').extract()
            for u1 in url1:
                yield Request(u1, callback=self.getUrl)

        for nurl2 in nurl2s:
            url2 = nurl2.xpath('li/dl/dt[@class="photo"]/a/@href').extract()
            for u2 in url2:
                yield Request(u2, callback=self.getUrl)

    def getUrl(self, response):
        item = ArticleItem()
        item['nurl'] = response.url
        item['aid'] = item['nurl'][-10:]
        item['press'] = response.xpath('//div[@class="press_logo"]/a/img/@title').extract()
        item['title'] = response.xpath('//h3[@id="articleTitle"]/text()').extract()
        item['date'] = response.xpath('//span[@class="t11"]/text()').extract()
        item['purl'] = response.xpath('//div[@class="sponsor"]/a/@href').extract()

        # After 01-25, Not working
        # item['nclass'] = response.xpath('//div[@id="snb"]/h2/a/text()').extract()
        item['nclass'] = response.xpath('//li[@class="on"]/a/span/text()').extract()

        # After 01-25, Not working
        # item['nclass2'] = response.xpath('//ul[@class="nav"]/li[@class="on"]/a/text()').extract()
        item['nclass2'] = ""

        if 'chosun' in item['purl'][0]:
            bodys = response.xpath('//div[@id="articleBodyContents"]')
            for body in bodys:
                item['body'] = " ".join(response.xpath('//p/text()').extract())
        else:
            item['body'] = " ".join(response.xpath('//div[@id="articleBodyContents"]/text()').extract())
        # item['num_comment'] = response.xpath('//span[@class="lo_txt"]/text()').extract()
        # item['num_recommend'] = response.xpath('//em[@class="u_cnt"]/text()').extract()

        return item