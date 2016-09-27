# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import hashlib
import urlparse

from bs4 import BeautifulSoup
from scrapy import Spider,Request
from scrapy.loader import ItemLoader

from rong.items import Rong360Item


def cleanBlank(*args):
    """公共函数,去除空格"""
    return [string.replace('\n','').replace('\r','').replace(' ','') for string in args]

def cleanBlankString(string):
    """公共函数,去除空格"""
    return string.replace('\n', '').replace('\r', '').replace(' ', '')

def getSignName(string):
    """返回签名"""
    return hashlib.sha1(string).hexdigest()


class Rong360Spider(Spider):
    name = "rong360"
    allowed_domains = ["rong360.com"]
    start_urls = (
        'http://www.rong360.com/licai-p2p/pingtai/rating',
    )

    def parse(self, response):
        """解析平台列表"""
        pass
        soup = BeautifulSoup(response.body,'html.parser')
        """
        names = response.xpath('//tbody[@id="ui_product_list_tbody"]/tr/td[@class="pt_name"]/a/text()').extract()
        pt_urls = response.xpath('//tbody[@id="ui_product_list_tbody"]/tr/td[@class="pt_name"]/a/@href').extract()
        gradeFromThirds = response.xpath('//tr/td[@class="pingji"]/text()').extract()
        profitAverages = response.xpath('//tbody[@id="ui_product_list_tbody"]/tr/td[@class="average"]/text()').extract()
        """
        names = [td.find('a').get_text() for td in soup.find_all('td',class_="pt_name")]
        pt_urls = [td.find('a').get('href') for td in soup.find_all('td',class_="pt_name")]
        gradeFromThirds = [td.get_text() for td in soup.find_all('td',class_="pingji")]
        profitAverages = [td.get_text() for td in soup.find_all('td',class_="average")]
        """清理空格"""
        names = cleanBlank(*names)
        pt_urls = cleanBlank(*pt_urls)
        gradeFromThirds = cleanBlank(*gradeFromThirds)
        profitAverages = cleanBlank(*profitAverages)
        for i in range(len(names)):
            yield Request(url=pt_urls[i],meta={'name':names[i],
                                               'gradeFromThird':gradeFromThirds[i],
                                               'profitAverage':profitAverages[i]
                                               },callback=self.parseDetail)
    def parseDetail(self,response):
        """解析详细页面,包含基本信息、简要介绍,管理团队,最新产品列表"""
        p_list = response.xpath('//div[@class="wrap-left wrap-clear"]/p')

        registeredCapital = p_list[1].xpath('text()').extract_first() #注册资金
        dateSale = p_list[3].xpath('text()').extract_first() #上线时间
        area = p_list[5].xpath('text()').extract_first() #区域
        url = p_list[7].xpath('a/@href').extract_first() #网址
        startMoney = p_list[9].xpath('text()').extract_first() #起投金额
        managementFee = p_list[11].xpath('text()').extract_first() #管理费
        cashTakingFee = p_list[13].xpath('text()').extract_first() #取现费用
        backGround = p_list[15].xpath('text()').extract_first() #平台背景
        provisionOfRisk = p_list[17].xpath('text()').extract_first() #风险准备金
        foundCustodian = p_list[19].xpath('text()').extract_first() #资金托管
        safeguardWay = p_list[21].xpath('text()').extract_first() #保障方式
        assignmentOfDebt = p_list[23].xpath('text()').extract_first() #债权转让
        automaticBidding = p_list[25].xpath('text()').extract_first() #自动投标
        cashTime = p_list[27].xpath('text()').extract_first() #提现到账时间

        """计算签名,作为标示字段"""
        url_data = urlparse.urlparse(url)
        """去掉协议，查询参数等"""
        url = url_data.netloc
        id = getSignName(url)

        """平台简介"""
        p_list2 = response.xpath('//div[@class="loan-msg-con tab-con"][1]/p')
        abstract = unicode(''.join(str(item) for item in p_list2.extract()),'utf-8')

        """接收额外数据"""
        name = response.meta['name']
        profitAverage = response.meta['profitAverage']
        gradeFromThird = response.meta['gradeFromThird']
        if not gradeFromThird:
            print '平台-------%s----------无法获取评级数据'%(name)

        """解析管理团队"""
        p_list3 = response.xpath('//div[@class="loan-msg-con tab-con"][2]/p')
        manageTeam = unicode(''.join(str(item) for item in p_list3.extract()),'utf-8')

        """解析最新产品"""
        li_list = response.xpath('//ul[@class="loan-product"]/li')
        products = [{'name':li.xpath('div/p[@class="p1"]/text()').extract_first(),
                     'annualizedReturn':li.xpath('div/p[@class="p2"]/span/text()').extract_first(),
                     'cycle':li.xpath('div/p[@class="p3"]/span/text()').extract_first(),
                     'process':li.xpath('div/p[@class="p4"]/span/text()').extract_first(),
                     'remainAmount':li.xpath('div/p[@class="p5"]/text()').extract_first(),
                     'platform_id':id,
                     } for li in li_list]

        """解析最新评论,暂时空缺"""
        pass

        """传入ITEM"""
        item = Rong360Item()
        item['id'] = id
        item['name'] = name
        item['gradeFromThird'] = gradeFromThird
        item['profitAverage'] = profitAverage
        item['dateSale'] = dateSale
        item['registeredCapital'] = registeredCapital
        item['area'] = area
        item['url'] = url
        item['startMoney'] = startMoney
        item['managementFee'] = managementFee
        item['cashTakingFee'] = cashTakingFee
        item['backGround'] = backGround
        item['provisionOfRisk'] = provisionOfRisk
        item['foundCustodian'] = foundCustodian
        item['safeguardWay'] = safeguardWay
        item['assignmentOfDebt'] = assignmentOfDebt
        item['automaticBidding'] = automaticBidding
        item['cashTime'] = cashTime
        item['abstract'] = abstract
        item['manageTeam'] = manageTeam
        item['products'] = products
        #item['reviews'] = '' #数据暂缺,后续补充
        yield item














