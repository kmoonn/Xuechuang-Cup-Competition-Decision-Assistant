# _*_ coding : utf-8 _*_
# @Time : 2023-03-28 21:49
# @Author : Kmoon_Hs
# @File : dev

import requests
import xlsxwriter as xw
from lxml import etree

import Money
import billnums

#老年1、青年2、白领3、商务4
custids = [4,3,2,1]
url = 'http://172.16.129.50:8088/BSTCS/student/CMO/C/CMO_C_5.jsp'
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
firscompanyid = 3460
companyids = [i for i in range(firscompanyid, firscompanyid + groups)]


# 获取每季度广告 每次请求一个公司某消费群体的广告投入
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
    result = tree.xpath('//td[@style="text-align:right"]/text()')
    return result

# 计算平均广告
def getCustAvgAd():
    list = getCustAd()
    products=getCustDevNum()
    for i in range(len(list)):
        # print(list[i],products[i]+"\n")
        # print(choose[i] +"平均广告投入:",round(list[i]/products[i]))
        print(choose[i] + "平均广告投入:", round(list[i] / 31))   #修改 实际小组数

# 获取每个消费群体的平均投入广告
def getCustAd():
    cust_Ad =[]
    for custid in custids:
        items = []
        sum = 0.00
        for companyid in companyids:
            result = getAdinput(companyid, custid)
            for item in result:
                item = item.strip()
                if item != '':
                    items.append(item)
        print(items)
        for i in items:
            if i != '':
                i = i.replace(',', '')
                i = i.replace('.00', '')
                sum = sum + float(i)
        cust_Ad.append(sum)
    return cust_Ad

# 获取产品研发情况
def getProductdev(companyid,custid):
    data = {
        'courseid': courseid,
        'companyid': companyid,
        'time': 1, # 季度
        'custid': custid, #老1 青2 白3 商4
        'studentid':4369 #格式必需
    }
    response = requests.get(url=url, params=data, headers=headers)
    content = response.text
    tree = etree.HTML(content)
    result = tree.xpath('//span/text()')
    return result

# 确定各消费群体产品数量
def getCustDevNum():
    cust_dev_nums=[]
    for custid in custids:
        items = []
        for companyid in companyids:
            result = getProductdev(companyid, custid)
            for item in result:
                items.append(item)
        # print(items)
        # print(len(items))
        cust_dev_nums.append(len(items))
    return cust_dev_nums

# 计算每个小组产品设计情况 确定每小组打法
def getGroupDevNum():
    for companyid in companyids:
        temp = [companyid]
        for custid in custids:
            result = getProductdev(companyid, custid)
            temp.append(len(result))
        print(temp) #设计情况
        groups_dev.append(temp)

# 各小组产品设计情况 写入excel
def xw_toExcel(data,filename):
    workbook = xw.Workbook(filename)
    worksheet1 = workbook.add_worksheet("sheet1")
    worksheet1.activate()
    title = ['companyid','商务','白领','青年','老年']
    i = 2
    worksheet1.write_row('A1',title)
    for j in data:
        row = 'A' + str(i)
        worksheet1.write_row(row,j)
        i=i+1
    workbook.close()


# 程序入口
if __name__ == '__main__':
        n = eval(input("请输入相应序号："))
        # 默认顺序：商务->白领->青年->老年
        '''
        可选功能
        - 1. getGroupDevNum 各小组产品设计情况
        - 2. getCustDevNum 各消费群体的产品设计数量    （第1，2季度）
        - 3. getCustAvgAd  每季度各消费群体广告投入情况  （翻季后，即季度初）
        - 4. getBillforMarket 未开市场小组订单数     （第3季度）
        - 5. getBillforRecognition 未资质认证小组订单数   （第3季度）
        - 6. getCompanyMoney 账款贴现    （交单完成之后）
        - 7. getProductEvaluation 产品评价 Todo
        '''
        if n==1:
            getGroupDevNum()
            filename = '各小组产品设计情况_t1.xlsx'  # 每季度产生一个excel
            xw_toExcel(groups_dev, filename)
        elif n==2:
            getCustDevNum()
        elif n==3:
            getCustAvgAd()
        elif n==4:
            billnums.getgetBillforMarket()
        elif n==5:
            billnums.getBillforRecognition()
        elif n==6:
            Money.getCompanyMoney()
        else:
            print("Action!")