# _*_ coding : utf-8 _*_
# @Time : 2023-03-30 14:32
# @Author : Kmoon_Hs
# @File : bill

import requests
from lxml import etree
import config as c

param = {'url':'','cookie':'','courseid':0,'companynums':0,'firstcompany':0,'choose':[],'custids':[],'headers':[],'mycompanyid':0}

c.Config(param)

url = 'http://%s/BSTCS/ReportAction.do' %param['url']
headers = param['headers']

def getBill(companyid,customerid):
    data = {
        'courseid': param['courseid'],  # 每次比赛不同id
        # 'studentid': 4936,
        'companyid':companyid,
        'customerid':customerid ,#all
        'totime':3,
        'fromtime':3,
        'action':0,
        'marketid':-1
    }
    response = requests.get(url=url, params=data, headers=headers)
    content = response.text
    tree = etree.HTML(content)
    result = tree.xpath('//tr[@class="tablebodytext"]/td[9]/text()')
    result = [str(item) for item in result]
    for i in range(0, len(result)):
        result[i] = result[i].replace(',', '')
        result[i] = eval(result[i].replace('.00', ''))
    return sum(result)


import dev
companyid_market = dev.getDict_market()
companyid_recognition = dev.getDict_Recognition()


def getgetBillforMarket():
    # 计算未开市场小组的订单数
    # print(companyid_market)
    print("未开市场小组数: ", sum(companyid_market.values()))
    for custid in [3,2,1]:
        noMarketBills = 0
        for companyid in companyid_market.keys():
            temp = (getBill(companyid,custid) * companyid_market[companyid])
            # print(temp)
            noMarketBills +=temp
        print("未开市场小组的订单量: ", noMarketBills)

def getBillforRecognition():
    # 计算未开资质小组的订单数
    # print(companyid_recognition)
    print("未开资质小组数: ", sum(companyid_recognition.values()))
    for custid in [1]:
        noRecognitionBills = 0
        for companyid in companyid_recognition.keys():
            temp = (getBill(companyid,custid) * companyid_recognition[companyid])
            noRecognitionBills += temp
        print("未开资质小组的订单量: ", noRecognitionBills)
