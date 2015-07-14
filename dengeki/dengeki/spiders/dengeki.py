#!/usr/bin/env python
# coding=utf-8
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sgml
#from dengeki.items import DengekiItem


class DengekiItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()


class DengekiSpider(scrapy.Spider):
    name = 'dengeki'
    #allowed_domain = ['cnblogs.com']
    #start_urls = ['www.cnblogs.com/renrenqq/archive/2010/09/09/1813669.html']
    start_urls = ['http://www.wenku8.cn/novel/1/1614/54757']
    allowed_domains = ["wenku8.cn"]

    def parse(self, response):
        items = []
        item = DengekiItem()
        sel = Selector(response)
        item['title'] = sel.xpath('/head/title')
        item['name'] = sel.xpath('/html/@xmlns')
        item['content'] = sel.xpath('ul[@id=contentdp]')

        file = open('content','w')
        json_content = json.dumps(dict(item),ensure_ascii = False)+'\n'
        file.write(json_content)
        print json_content
