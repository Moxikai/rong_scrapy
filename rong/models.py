#!/usr/bin/env python
# coding:utf-8
"""


"""
import os

from sqlalchemy import Column, create_engine, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

_baseDir = os.path.dirname(__file__)

_engine = create_engine('sqlite:///' + os.path.join(_baseDir, 'data-dev.db'))
Base = declarative_base()

_DBsession = sessionmaker(bind=_engine)
session = _DBsession()


class Law(Base):
    """法律信息"""
    __tablename__ = 'law'

    id = Column(String(48),primary_key=True)
    title = Column(String(48))
    type = Column(String(48))
    publishDepartment = Column(String(48))
    publishDate = Column(String(48))
    effectDate = Column(String(48))
    loseEffectDate = Column(String(48))
    status = Column(String(48))
    content = Column(Text)

class Platform(Base):
    """平台信息"""
    __tablename__ = 'platform'

    id = Column(String(48),primary_key=True)
    name = Column(String(48))
    gradeFromThird = Column(String(48))
    profitAverage = Column(String(48))
    dateSale = Column(String(48))
    registeredCapital = Column(String(48))
    area = Column(String(48))
    url = Column(String(48))
    startMoney = Column(String(48))
    managementFee = Column(String(48))
    cashTakingFee = Column(String(48))
    backGround = Column(String(48))
    provisionOfRisk = Column(String(48))
    foundCustodian = Column(String(48))
    safeguardWay = Column(String(48))
    assignmentOfDebt = Column(String(48))
    automaticBidding = Column(String(48))
    cashTime = Column(String(48))
    abstract = Column(Text)
    manageTeam = Column(Text)
    #persons = relationship('Person',backref='platform')
    #products = relationship('Product',backref='platform')
    #companys = relationship('Company',backref='platform')

class Product(Base):
    """产品信息"""
    __tablename__ = 'product'

    id = Column(String(48),primary_key=True)
    name = Column(String(48))
    annualizedReturn = Column(String(48)) #年化收益率
    cycle = Column(String(48)) #投资周期
    remainAmount = Column(String(48)) #剩余额度
    platform_id = Column(String(48),ForeignKey('platform.id'))

class Company(Base):
    """新增公司信息"""
    __tablename__ = 'company'

    id = Column(String(48),primary_key=True)
    platformName = Column(String(48)) #冗余字段
    companyName = Column(String(48))
    legalRepresentative = Column(String(48))
    QQ = Column(String(48))
    phoneCustomer = Column(String(48))
    address = Column(String(128))
    noteSpecial = Column(Text)
    platform_id = Column(String(48))



def init_db():
    
    Base.metadata.create_all(_engine)


def drop_db():

    Base.metadata.drop_all(_engine)


if __name__ == '__main__':

    drop_db()
    init_db()
