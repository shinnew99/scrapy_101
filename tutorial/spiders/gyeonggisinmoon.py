# #-*- coding: utf-8 -*-
#
# import re
# import datetime
# import scrapy
# # import urlparse
# # from urllib import urlencode
#
# from tutorial.items import ArticleItem
#
#
#
# class GyeonggiSinmoon(scrapy.Spider):
#     name = 'ggs'
#     allowed_domains = ["www.kgnews.co.kr"]
#     url = u'http://www.kgnews.co.kr/engine_yonhap/search.php?'
#     parsed_url = urlparse.urlparse(url)
#     params = {
#         'period': 'all',
#         'from_date': '2015-05-12',
#         'to_date': '2015-12-30',
#         'searchword': u'메르스'.encode('euc-kr'),
#         'picktab': 'article',
#         'sort': 'date'
#     }
#
#     def start_requests(self):
#
#         yield scrapy.Request(url=self.url + urlencode(self.params), callback=self.parse_last)
#
#     def parse_last(self, response):
#         last_url = response.css('a.nnext::attr(href)').extract_first()
#
#         if last_url is None:
#             print(response.url)
#             return
#
#         parsed = urlparse.urlparse(last_url)
#
#         last_page = urlparse.parse_qs(parsed.query)['page'][0]
#         if last_page is None:
#             return
#
#         for i in range(1, int(last_page)+1):
#             yield scrapy.Request(url=self.url+ urlencode(self.params) + '&page='+str(i), callback=self.parse)
#
#     def parse(self, response):
#         hrefs = []
#         list_df = response.css('div.contents')
#         lists = list_df.css('strong.title')
#         for quote in lists:
#             href = quote.css('a::attr(href)').extract_first()
#             hrefs.append(href)
#         for href in hrefs:
#             yield scrapy.Request(href, callback=self.parse_view)
#
#     def parse_view(self, response):
#
#         item = ArticleItem()
#         pattern = re.compile(r'\s+')
#         pattern2 = re.compile(r'\t')
#         pattern3 = re.compile(r'\n')
#         pattern4 = re.compile(u"<.*?>|&nbsp;|&amp;|\u260e", re.DOTALL | re.M)
#         pattern5 = re.compile(r'\W')
#
#         parsed = urlparse.urlparse(response.url)
#
#         item['aid'] = int(urlparse.parse_qs(parsed.query)['idxno'][0])
#         item['nUrl'] = ''
#         item['press'] = unicode('경기신문', 'utf-8')
#
#         item['title'] = response.css('div.View_Title strong::text').extract_first()
#         news_date = response.css('div.View_Time::text').extract_first()
#         news_date = re.sub(pattern5, '', news_date)
#
#         news_date = datetime.datetime.strptime(str(news_date.encode('UTF-8')), '%Y%m%d%H%M%S')
#         news_date = news_date.strftime('%Y-%m-%d %H:%M:%S')
#         item['aDate'] = news_date
#         item['pUrl'] = response.url
#         item['nClass'] = 'mers'
#         # item['nclass2'] = response.css('div#newsitem_head h4 a::text').extract()
#         item['subClass'] = ''
#         item['numComment'] = ''
#         item['content'] = ''
#         contents = response.css('td#articleBody::text').extract()
#         for content in contents:
#             item['content'] += content
#         item['pdf'] = ''
#         item['html']=''
#         return item
