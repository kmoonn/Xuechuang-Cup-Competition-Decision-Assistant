# _*_ coding : utf-8 _*_
# @Time : 2023-03-29 14:12
# @Author : Kmoon_Hs
# @File : dev

import requests
from lxml import etree

# 设置cookie
cookie  = '63FBDE02DB70B4886D4F54E76C78A260'

url = 'http://ishapan.com:9099/BSTCS/student/CEO/B/CEO_B_4.jsp'
data = {
    'courseid': 358,  # 每次比赛不同id
    'studentid': 4936,
    }
headers = {
    'Cookie': 'JSESSIONID=%s' % cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

# 市场开发情况  投资表现
def getmarketDev():
    response = requests.get(url=url, params=data, headers=headers)
    content = response.text
    tree = etree.HTML(content)
    companyid = tree.xpath('//tr[@class="tablebodytext"]/td[2]/script/text()')
    companyid = [str(item).strip()[21:25] for item in companyid]
    result = tree.xpath('//tr[@class="tablebodytext"]/td[6]/text()')
    result = result[:-1]
    result = [str(item) for item in result]
    for i in range(0, len(result)):
        result[i] = result[i].replace(',', '')
        result[i] = eval(result[i].replace('.00', ''))
    return result,companyid


# 资质认证情况
def getRecognition():
    response = requests.get(url=url, params=data, headers=headers)
    content = response.text
    tree = etree.HTML(content)
    result = tree.xpath('//tr[@class="tablebodytext"]/td[5]/text()')
    result = result[:-1]
    result=[str(item) for item in result]
    companyid = tree.xpath('//tr[@class="tablebodytext"]/td[2]/script/text()')
    companyid = [str(item).strip()[21:25] for item in companyid]
    for i in range(0,len(result)):
        result[i] = result[i].replace(',', '')
        result[i] = eval(result[i].replace('.00', ''))
    return result,companyid

companyid_market = {}
companyid_recognition = {}

def getDict_market():
    result,companyids = getmarketDev()
    for i in range(len(result)):
        money = int(result[i])
        if money<180000:
            companyid_market[companyids[i]]= 2
        elif 180000 <= money < 240000:
            companyid_market[companyids[i]] = 1
        else:
            companyid_market[companyids[i]] = 0
    return companyid_market

def getDict_Recognition():
    result,companyids = getRecognition()
    for i in range(len(result)):
        money = int(result[i])
        if money<60000:
            companyid_recognition[companyids[i]] = 1
        else:
            companyid_recognition[companyids[i]] = 0
    return companyid_recognition
