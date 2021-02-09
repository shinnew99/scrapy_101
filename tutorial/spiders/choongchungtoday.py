# -*- coding: utf-8 -*-


import scrapy
import re
from tutorial.items import ArticleItem

# import urlparse


class ChoongChungToday(scrapy.Spider):
    name = 'cct'
    allowed_domains = ["www.cctoday.co.kr"]
    url = u'http://www.cctoday.co.kr?mod=search&act=engine&cust_div_code=&searchContType=article&searchWord=메르스&fromDate=2015-05-01&toDate=2015-12-30&sfield=&article_type=&sort=date'

    def start_requests(self):

        yield scrapy.Request(url=self.url, callback=self.parse_last)

    def parse_last(self, response):
        last_url = response.css('a.p_last::attr(href)').extract_first()

        if last_url is None:
            return

        for i in range(1, 99):
            yield scrapy.Request(url=self.url+'&page='+str(i), callback=self.parse)

    def parse(self, response):
        hrefs = []
        for quote in response.css('a.title_a::attr(href)').extract():
            hrefs.append(quote)

        for href in hrefs:
            next_page = response.urljoin(href)
            yield scrapy.Request(next_page, callback=self.parse_view)

    def parse_view(self, response):

        # item = ArticleItem()
        # pattern = re.compile(r'\s+')
        # pattern2 = re.compile(r'\t')
        # pattern3 = re.compile(r'\n')
        # parsed = urlparse.urlparse(response.url)
        #
        # item['aid'] = int(urlparse.parse_qs(parsed.query)['idxno'][0])
        # item['press'] = unicode('충청투데이', 'utf-8')
        # text = response.css('h1.arl_view_title::text').extract_first()
        # text = re.sub(pattern2, '', text)
        # text = re.sub(pattern3, '', text)
        # item['title'] = text
        # text = response.css('span.arl_view_date::text').extract_first()
        # text = re.sub(pattern, '', text)
        # year = text[:4]
        # month = text[5:7]
        # day = text[8:10]
        # real_day = year+'-'+month+'-'+day
        #
        # item['aDate'] = real_day
        # item['pUrl'] = response.url
        # item['nUrl'] = ''
        # item['nClass'] = 'mers2'
        # item['subClass'] = ''
        # item['content'] = response.css('div#adiContents::text').extract_first()
        # item['numComment'] = ''
        # item['pdf'] = ''
        # item['html'] = ''

        return item
