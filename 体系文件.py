import requests
from bs4 import BeautifulSoup
import random
import json
import re
from lxml import etree

import os
# def
url = 'http://oa.bears.com.cn:27292/km/institution/km_institution_knowledge/kmInstitutio' \
      'nKnowledgeIndex.do?method=listChildren&categoryId=15dbf410dca548412ab6' \
      '4024e8bb4521&q.docStatus=30&orderby=docC' \
      'reateTime&o' \
      'rdertype=down&__seq=1599054519269&s_ajax=true'

# url = 'http://oa.bears.com.cn:27292/km/institution/?categoryId=15dbf410dca548412ab64024e8bb4521#cri.q=docStatus:30'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

cookies = {'Cookie': 'j_lang=zh-CN; JSESSIONID=6E16932E1745472E3DC172420CED1BED; LtpaToken=AAECAzVGNTc4MUI0NU'
                     'Y1ODJBNzR6aGFvbGaxQFyg6/I8UqXwMGCxmRsqsA7M6A=='}
#翻页
# num = range(2,13)
num = [2,3]
for i in num:
    params = {'method': 'listChildren',
                            'categoryId': '15dbf410dca548412ab64024e8bb4521',
                            'q.docStatus': '30',
                            'q.s_raq': 0.4455115328171888,
                            'pageno': i,
                            'rowsize': 15,
                            'orderby': 'docCreateTime',
                            'ordertype': 'down',
                            's_ajax': 'true'}
    response = requests.get(url,headers=headers,cookies=cookies,params=params)
    html = response.text
    # params
    # query_string_parameters
    #循环打印列表关键信息
    data = json.loads(html)
    # print(data['datas'])
    for i in data['datas']:

        id = i[0]['value']
        title = i[2]['value']
        fdNumber = i[3]['value']
        bm = i[6]['value']
        name =i[7]['value']
        time = i[8]['value']
        name = re.findall('>.*<',name)[0].replace('<','').replace('>','')

        print('ID:{}:文件名称:{} \n文件编号:{} 所属部门:{} 录入者：{} 生效时间:{}\n'.format(id,title,fdNumber,bm,name,time))
        #待做：将以上7个关键字段格式化，并返回信息




#生成随机数
    # a = random.uniform(0, 0.05)
    # print(a)