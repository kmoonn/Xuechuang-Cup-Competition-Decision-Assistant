# _*_ coding : utf-8 _*_
# @Time : 2023-03-30 22:50
# @Author : Kmoon_Hs
# @File : Evaluation

import requests
from lxml import etree

# 设置cookie
cookie  = 'BD1A559A8EE07227B9F883F0D9C12D91'

url = 'http://172.16.129.50:8088/BSTCS/student/CMO/C/CMO_C_1.jsp'
data = {
    'courseid': 387,  # 每次比赛不同id
    # 'studentid': 496,
    'companyid':3469,
    # 'time':1
    }
headers = {
    'Cookie': 'JSESSIONID=%s' % cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}


def getProductEvaluation():
    response = requests.get(url=url, params=data, headers=headers)
    content = response.text
    tree = etree.HTML(content)
    result = tree.xpath('//tr[@class="tablebodytext"]/td[2]/text()')
    qq = tree.xpath('//tr[@class="tablebodytext"]/td[5]/text()')
    result = result[:-1]
    result = [str(item) for item in result]
    for i in range(0, len(result)):
        result[i] = result[i].replace(',', '')
        result[i] = eval(result[i].replace('.00', ''))
