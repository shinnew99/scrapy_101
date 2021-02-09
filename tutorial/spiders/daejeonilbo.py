# -*- coding: utf-8 -*-

import re
import datetime
import scrapy
# import urlparse
import base64

from tutorial.items import ArticleItem



class DaejeonIlbo(scrapy.Spider):
    name = 'dji'
    allowed_domains = ["www.daejonilbo.com"]

    url = u'http://www.daejonilbo.com/ksearch/search.asp?kwd=%B8%DE%B8%A3%BD%BA&xwd=&pageNum=1&pageSize=10000&category=NEWS&subCategory=00&reSrchFlag=false&sort=d&searchRange=a&detailSearch=false&detailDate=0&startDate=20150501&endDate=20151230&srchFd=all&paperNum=&PDFpaperNum=&startHit=&sliderCheck=30&groupsearch=all&preKwd=%B8%DE%B8%A3%BD%BA'

    def start_requests(self):

        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):

        hrefs = []
        list_df = response.css('ul.list_df')[0]
        for quote in list_df.css('a::attr(href)').extract():
            hrefs.append(quote)

        for href in hrefs:
            yield scrapy.Request(href, callback=self.parse_view)

    def parse_view(self, response):

        # item = ArticleItem()
        # pattern = re.compile(r'\s+')
        # pattern2 = re.compile(r'\t')
        # pattern3 = re.compile(r'\n')
        #
        # parsed = urlparse.urlparse(response.url)
        #
        # item['nUrl'] = ''
        # item['aid'] = int(urlparse.parse_qs(parsed.query)['pk_no'][0])
        #
        # item['press'] = u('대전일보', 'utf-8')
        #
        # item['title'] = response.css('div#newsitem_head h1::text').extract_first()
        # text = response.css('div#newsitem_head h5::text').extract_first()
        # mydatetime = datetime.datetime.strptime(text[:-3], '%Y-%m-%d')
        # text = mydatetime.strftime('%Y-%m-%d %H:%M:%S')
        # item['aDate'] = text
        # item['pUrl'] = response.url
        # item['nClass'] = 'mers'
        # # item['nclass2'] = response.css('div#newsitem_head h4 a::text').extract()
        # item['subClass'] = ''
        # item['numComment'] = ''
        # item['content'] = response.css('div#fontSzArea::text').extract_first()
        # item['pdf'] = ''
        # item['html'] = ''
        return item
