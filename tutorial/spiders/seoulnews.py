#-*- coding: utf-8 -*-

import scrapy
import re
from operator import eq
from tutorial.items import ArticleItem


class DoctorsNews(scrapy.Spider):
    name = 'sn'
    allowed_domains = ["seoul.co.kr", "go.seoul.co.kr"]
    url = u'http://search.seoul.co.kr/index.php?scope=&sort=&cpCode=seoul;nownews&period=&sDate=2015-01-01&eDate=2015-12-31&keyword=%EB%A9%94%EB%A5%B4%EC%8A%A4&iCategory=&pCategory=undefined&'

    def start_requests(self):
        for i in range(1, 333):
            yield scrapy.Request(url=self.url+'pageNum='+str(i)+'?page=1', callback=self.parse)

    def parse(self, response):
        hrefs = []
        for quote in response.css('dl.article dt a::attr(href)').extract():
            hrefs.append(quote)

        for href in hrefs:
            yield scrapy.Request(url=href, callback=self.parse_view)

    def parse_view(self, response):
        item = ArticleItem()
        pattern = re.compile(r'\s+')
        pattern2 = re.compile(r'\t')
        pattern3 = re.compile(r'\n')

        item['aid'] = int(response.url[-6:])
        item['press'] = str('서울신문')
        if eq((response.url)[7:9], 'ww'):
            text = response.css('div.atit2::text').extract_first()
            text = re.sub(pattern2, '', text)
            text = re.sub(pattern3, '', text)
            item['title'] = text

            text = response.css('p.v_days::text').extract_first()
            text = re.sub(pattern, '', text)
            text = text[3:13]
            item['aDate'] = text + ' 00:00'

            text = response.css('div#atic_txt1.v_article p::text').extract_first()
            temp = response.css('div#atic_txt1.v_article::text').extract()
            for i in temp:
                text += ' ' + i
            text = re.sub(pattern2, '', text)
            text = re.sub(pattern3, '', text)
            item['content'] = text

        elif eq((response.url)[7:9], 'go'):
            text = response.css('h3.title_main::text').extract_first()
            text = re.sub(pattern2, '', text)
            text = re.sub(pattern3, '', text)
            item['title'] = text

            text = response.css('div.tsocial span::text').extract_first()
            text = re.sub(pattern, '', text)
            text = text[3:13]
            item['aDate'] = text

            temp = response.css('div.atic_txt1::text, div.atic_txt1 p::text').extract()
            text = ''
            for i in temp:
                text += ' ' + i
            item['content'] = text
            text = re.sub(pattern2, '', text)
            text = re.sub(pattern3, '', text)
            item['content'] = text

        item['pUrl'] = response.url
        item['nUrl'] = ''
        item['nClass'] = 'mers3'
        item['subClass'] = ''
        item['numComment'] = ''
        item['pdf'] = ''
        item['html'] = ''

        return item

