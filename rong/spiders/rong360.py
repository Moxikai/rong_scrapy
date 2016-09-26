# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.loader import ItemLoader

from rong.items import PersonItem,PlatformItem,ProductItem


def cleanBlank(*args):
    """公共函数,去除空格"""
    return [item.replace('\n','').replace('\r','').replace(' ','') for item in args]

class Rong360Spider(Spider):
    name = "rong360"
    allowed_domains = ["rong360.com"]
    start_urls = (
        'http://www.rong360.com/licai-p2p/pingtai/rating',
    )

    def parse(self, response):
        """解析平台列表"""
        pass
        names = response.xpath('//tbody[@id="ui_product_list_tbody"]/tr/td[@class="pt_name"]/a/text()').extract()
        pt_urls = response.xpath('//tbody[@id="ui_product_list_tbody"]/tr/td[@class="pt_name"]/a/@href').extract()
        gradeFromThirds = response.xpath('//tbody[@id="ui_product_list_tbody"]/tr/td[@class="pingji"]/text()').extract()
        profitAverages = response.xpath('//tbody[@id="ui_product_list_tbody"]/tr/td[@class="average"]/text()').extract()
        names = cleanBlank(*names)
        pt_urls = cleanBlank(*pt_urls)
        gradeFromThirds = cleanBlank(*gradeFromThirds)
        profitAverages = cleanBlank(*profitAverages)
        for i in range(len(names)):
            yield {
            'name':names[i],
            'pt_url':pt_urls[i],
            'gradeFromThird':gradeFromThirds[i],
            'profitAverage':profitAverages[i],
        }


