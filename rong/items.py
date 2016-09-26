# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item,Field

class Rong360Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = Field()
    name = Field()
    gradeFromThird = Field()
    profitAverage = Field()
    dateSale = Field()
    registeredCapital = Field()
    area = Field()
    url = Field()
    startMoney = Field()
    managementFee = Field()
    cashTakingFee = Field()
    backGround = Field()
    provisionOfRisk = Field()
    foundCustodian = Field()
    safeguardWay = Field()
    assignmentOfDebt = Field()
    automaticBidding = Field()
    cashTime = Field()
    abstract = Field() #平台简介,类型为字符串
    manageTeam = Field() #管理团队,类型为字符串
    products = Field() #产品,类型为list
    #reviews = Field() #评论,类型为list