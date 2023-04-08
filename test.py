# _*_ coding : utf-8 _*_
# @Time : 2023-03-28 21:43
# @Author : Kmoon_Hs
# @File : test
'''
GET /BSTCS/student/CMO/C/CMO_C_5.jsp?courseid=372&companyid=-1&studentid=5468&time=5&title=¹ã¸æÍ¶·Å HTTP/1.1
Accept: */*
Referer: http://ishapan.com:9099/BSTCS/bststart/student/CMO/left.jsp?courseid=370&databasename=bsterbstpcs&studentid=5468&companyid=2742
Accept-Language: zh-Hans-CN,zh-Hans;q=0.5
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0)
Host: ishapan.com:9099
Cookie: JSESSIONID=65C589E208701199BBC60D7A2E63976B
Connection: close
'''

import requests
from lxml import etree
import config as c

param = {'url':'','cookie':'','courseid':0,'companynums':0,'firstcompany':0,'choose':[],'custids':[],'headers':[],'mycompanyid':0}

c.Config(param)

headers = param['headers']

url = 'http://%s/BSTCS/student/CMO/C/CMO_C_5.jsp' %param['url']
data = {
    'courseid': param['courseid'],  # 每次比赛不同id
    'studentid': 1082,
    'time':5,
    'companyid':'§№☆●◎□◆○◎★▲△■※￡¤￠℃￥ξοωχυλβιμητσ',
    'custid':'§№☆●◎□◆○◎★▲△■※￡¤￠℃￥ξοωχυλβιμητσ'
    }

def getCustAvgAd(time):
    response = requests.get(url=url, params=data, headers=headers)
    content = response.text
    tree = etree.HTML(content)
    result = tree.xpath('//tr[@style="display:none"]/td[%s]/text()') %time
    result = [str(item).strip() for item in result]
    for i in range(0, len(result)):
        result[i] = result[i].replace(',', '')
        result[i] = result[i].replace('.00', '')
    return result

getCustAvgAd(1)
