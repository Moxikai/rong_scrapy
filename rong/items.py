# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class PlatformItem(Item):
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
    abstract = Field()

class PersonItem(Item):
    pass
    id = Field()
    abstracts = Field()
    platform_id = Field()


class ProductItem(Item):
    pass
    id = Field()
    name = Field()
    annualizedReturn = Field()
    cycle = Field()
    remainAmount = Field()
    platform_id = Field()