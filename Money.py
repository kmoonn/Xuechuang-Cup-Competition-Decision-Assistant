# _*_ coding : utf-8 _*_
# @Time : 2023-03-30 14:48
# @Author : Kmoon_Hs
# @File : Money

import requests
from lxml import etree
import config as c

param = {'url':'','cookie':'','courseid':0,'companynums':0,'firstcompany':0,'choose':[],'custids':[],'headers':[],'mycompanyid':0}

c.Config(param)

headers = param['headers']

url = 'http://%s/BSTCS/student/CFO/A/CFO_A_1.jsp' %param['url']
data = {
    'courseid': param['courseid'],  # 每次比赛不同id
    'studentid': 4096,
    'companyid':param['mycompanyid'],
    # 'time':1
    }

# 市场开发情况  投资表现
def getCompanyMoney():
    Q1 = 0
    Q2 = 0
    Q3 = 0
    response = requests.get(url=url, params=data, headers=headers)
    content = response.text
    tree = etree.HTML(content)
    result = tree.xpath('//tr[@class="tablebodytext"]/td[2]/text()')
    qq = tree.xpath('//tr[@class="tablebodytext"]/td[5]/text()')
    result = [str(item) for item in result]
    for i in range(0, len(result)):
        result[i] = result[i].replace(',', '')
        result[i] = eval(result[i].replace('.00', ''))
    for j in range(len(result)):
        if qq[j] == "1季度":
            Q1 += result[j]
        elif qq[j] == "2季度":
            Q2 +=result[j]
        else:
            Q3+= result[j]
    print(Q1,Q2,Q3)