# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from rong.models import Platform,Product,session
from rong.spiders.rong360 import getSignName
class CleanDataPipeline():
    pass

class PlatformBasicSQLitePipeline():
    """保存平台基本信息至sqlite数据库"""
    def process_item(self, item, spider):
        platforms = session.query(Platform).filter(Platform.id == item['id']).all()
        if platforms:
            #更新
            session.query(Platform).filter(Platform.id == item['id']).update({
                'gradeFromThird': item['gradeFromThird'],
                'profitAverage': item['profitAverage'],
                'dateSale': item['dateSale'],
                'registeredCapital': item['registeredCapital'],
                'area': item['area'],
                'url': item['url'],
                'startMoney': item['startMoney'],
                'managementFee': item['managementFee'],
                'cashTakingFee': item['cashTakingFee'],
                'backGround': item['backGround'],
                'provisionOfRisk': item['provisionOfRisk'],
                'foundCustodian': item['foundCustodian'],
                'safeguardWay': item['safeguardWay'],
                'assignmentOfDebt': item['assignmentOfDebt'],
                'automaticBidding': item['automaticBidding'],
                'cashTime': item['cashTime'],
                'abstract': item['abstract'],
                'manageTeam': item['manageTeam'],
            })
            print '平台-----%s------更新完毕'%(item['name'])
        else:

            new_platform = Platform(id = unicode(str(item['id']),'utf-8'),
                                name = item['name'],
                                gradeFromThird = item['gradeFromThird'],
                                profitAverage = item['profitAverage'],
                                dateSale = item['dateSale'],
                                registeredCapital = item['registeredCapital'],
                                area = item['area'],
                                url = item['url'],
                                startMoney = item['startMoney'],
                                managementFee = item['managementFee'],
                                cashTakingFee = item['cashTakingFee'],
                                backGround = item['backGround'],
                                provisionOfRisk = item['provisionOfRisk'],
                                foundCustodian = item['foundCustodian'],
                                safeguardWay = item['safeguardWay'],
                                assignmentOfDebt = item['assignmentOfDebt'],
                                automaticBidding = item['automaticBidding'],
                                cashTime = item['cashTime'],
                                abstract = item['abstract'],
                                manageTeam = item['manageTeam'],
                                )
            session.add(new_platform)
            session.commit()
            print '平台------%s--------新增完毕'%(item['name'])

        return item




class PlatformProductSQLitePipeline():
    """保存平台产品信息至sqlite数据库"""
    def process_item(self,item,spider):
        products = item['products']
        if not products:
            print '平台：-----%s------暂时无产品'%(item['name'])
        else:
            for product in products:
                """计算签名"""
                id = getSignName(product['name'])
                new_product = Product(id=id,
                                      name=product['name'],
                                      annualizedReturn=product['annualizedReturn'],
                                      cycle=product['cycle'],
                                      process=product['process'],
                                      remainAmount=product['remainAmount'],
                                      platform_id=product['platform_id'],)
                product0 = session.query(Product).filter(Product.id == id).first()
                if product0:
                    pass
                    session.query(Product).filter(Product.id == product['id']).update({
                        'annualizedReturn':product['annulizedReturn'],
                        'cycle':product['cycle'],
                        'process':product['process'],
                        'remainAmount':product['remainAmount'],
                        'platform_id':product['platform_id'],
                    })
                    print '平台：-----%s------产品：-------%s--------更新完毕'%(item['name'],product['name'])
                else:
                    session.add(new_product)
                    session.commit()
                    print '平台：-----%s-----产品：------%s-------新增完毕'%(item['name'],product['name'])

        return item




