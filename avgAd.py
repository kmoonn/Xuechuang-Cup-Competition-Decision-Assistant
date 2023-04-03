# _*_ coding : utf-8 _*_
# @Time : 2023-03-31 19:51
# @Author : Kmoon_Hs
# @File : avgAd

import requests
from lxml import etree


# 获取各小组当季广告投入情况

#老年1、青年2、白领3、商务4
custids = [4,3,2,1]
url = 'http://172.16.129.50:8088/BSTCS/student/CMO/A/CMO_A_2.jsp'
# 设置cookie
cookie  = 'BD1A559A8EE07227B9F883F0D9C12D91'

headers = {
    'Cookie': 'JSESSIONID=%s' % cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

choose =["商务","白领","青年","老年"]

groups_dev = []
courseid = 387

# 设置小组数
groups = 37
# 设置起始公司 firstid
firscompanyid = 2631
companyids = [i for i in range(firscompanyid, firscompanyid + groups)]

def getAdinput(companyid,custid):
    data = {
        'courseid': '%s' % courseid, #每次比赛不同id
        'companyid': '%s' % companyid, #公司id
        'time': 1, # 季度
        'custid':'%s' % custid,
        'studentid': 4369  # 格式必需
    }
    response = requests.get(url=url, params=data, headers=headers)
    content = response.text
    tree = etree.HTML(content)
    result = tree.xpath('//a/text()')
    for item in result:
        item.strip()
    return result

print(getAdinput(2660,4))