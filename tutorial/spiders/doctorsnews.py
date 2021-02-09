# #-*- coding: utf-8 -*-
#
# #import urllib.parse as urlparse
# import scrapy
# import re
# import datetime
# from tutorial.items import ArticleItem
#
#
# class DoctorsNews(scrapy.Spider):
#     name = 'dn'
#     allowed_domains = ["doctorsnews.co.kr"]
#     url1 = u'http://www.doctorsnews.co.kr/news/articleList.html'
#     url2 = u'&total=893&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_add_section_code=&sc_add_sub_section_code=&sc_add_serial_code=&sc_area=A&sc_level=&sc_m_level=&sc_article_type=&sc_view_level=&sc_sdate=2015-1-1&sc_edate=2015-12-31&sc_serial_number=&sc_word=%B8%DE%B8%A3%BD%BA&sc_word2=&sc_andor=OR&sc_order_by=I&view_type='
#     url3 = u'http://www.doctorsnews.co.kr/news/'
#
#     def start_requests(self):
#         for i in range(1, 40):
#             yield scrapy.Request(url=self.url1+'?page='+str(i)+self.url2, callback=self.parse)
#
#     def parse(self, response):
#         hrefs = []
#         for quote in response.css('a.news_list_title::attr(href)').extract():
#             hrefs.append(quote)
#
#         for href in hrefs:
#             url = self.url3+href
#             url = url[:-12]
#             yield scrapy.Request(url=url, callback=self.parse_view)
#
#     def parse_view(self, response):
#         item = ArticleItem()
#         pattern = re.compile(r'\s+')
#         pattern2 = re.compile(r'\t')
#         pattern3 = re.compile(r'\n')
#
#         item['aid'] = int(response.url[-6:])
#         item['press'] = str('의협신문')
#         text = (response.css('td#font_title.title::text').extract())[1]
#         text = re.sub(pattern2, '', text)
#         text = re.sub(pattern3, '', text)
#         item['title'] = text
#
#         text = (response.css('span.SmN::text').extract())[0]
#         text = re.sub(pattern, '', text)
#         text = text[:-8]
#         text = text.replace('.', '-')
#         item['aDate'] = text + ' 00:00'
#
#         item['pUrl'] = response.url
#         item['nUrl'] = ''
#         item['nClass'] = 'mers3'
#         item['subClass'] = ''
#
#         temp = response.css('div.articleBody p::text').extract()
#         text = ''
#         for i in temp:
#             text += ' ' + i
#         item['content'] = text
#
#         item['numComment'] = ''
#         item['pdf'] = ''
#         item['html'] = ''
#
#         return item
