import requests
from bs4 import BeautifulSoup
import random

import json
import re
from lxml import etree
from selenium import webdriver
import os
import time


def get_infomation(url):


    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

    cookies = {'Cookie': 'j_lang=zh-CN; JSESSIONID=6CF942E6E6F659F055A3D9E1583AE7D9; LtpaToken=AAECAzVGNkNBQkRDNUY2RD'
                         'U0OUN6aGFvbGbaCjAFzC7a/i6Nrbtah23OZgeUbg=='}
    #翻页
    # num = range(2,13)
    num = [2,3]
    nums = random.uniform(0,0.05)

    for i in num:
        params = {'method': 'listChildren',
                                'categoryId': '15dbf410dca548412ab64024e8bb4521',
                                'q.docStatus': '30',
                                'q.s_raq': nums,
                                'pageno': i,
                                'rowsize': 15,
                                'orderby': 'docCreateTime',
                                'ordertype': 'down',
                                's_ajax': 'true'}
        response = requests.get(url,params=params,headers=headers,cookies=cookies)

        html = response.text
        # params
        # query_string_parameters
        #循环打印列表关键信息
        # print(html)
        data = json.loads(html)


        information = {}
        page_urls = []
        for i in data['datas']:

            id = i[0]['value']
            title = i[2]['value']
            fdNumber = i[3]['value']
            bm = i[6]['value']
            name =i[7]['value']
            time = i[8]['value']
            name = re.findall('>.*<',name)[0].replace('<','').replace('>','')

            # print('ID:{}:文件名称:{} \n文件编号:{} 所属部门:{} 录入者：{} 生效时间:{}\n'.format(id,title,fdNumber,bm,name,time))
            # 待做：将以上7个关键字段格式化，并返回信息
            information['id'] = id
            information['title'] = title
            information['fdNumber'] = fdNumber
            information['bm'] = bm
            information['name'] = name

        #页面中的行链接
            page_url = 'http://oa.bears.com.cn:27292/km/institution/km_institution_knowledge/kmInstitutionKn' \
              'owledge.do?method=view&fdId='+information['id']
            page_urls.append(page_url)

        return page_urls




def webget(url):


    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
    #打开文件页面（批量获取文件页面？？？？？）
    # 引入page行链接
    page_url = get_infomation(url)
    for url in page_url:

        # for url in infomation:

        #配置浏览器不打开页面，只在后台运行
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('disable-gpu')
        # chrome_options = chrome_options
        chrome = webdriver.Chrome()
        chrome.get(url)

        # 输入账号密码
        name = chrome.find_element_by_name('j_username')
        password = chrome.find_element_by_name('j_password')
        name.send_keys('zhaolf')
        password.send_keys('19921231Zlf')
        #
        # # 执行登录
        login_button = chrome.find_element_by_class_name("lui_login_button_div_c")
        login_button.click()
        html = chrome.page_source
        cookies = chrome.get_cookies()  # 利用selenium原生方法得到cookies
        ret = ''

        #捕获拼接登录所用的cookies
        for cookie in cookies:
            cookie_name = cookie['name']
            cookie_value = cookie['value']
            ret = ret + cookie_name + '=' + cookie_value + ';'  # ret即为最终的cookie，各cookie以“;”相隔开
        a = {}
        #将cookies写入字典中
        cookie = a['cookies'] = '{}'.format(ret)
        code = etree.HTML(html)
        imp = code.xpath("//table[@id='att_xtable_attachment']/tbody/tr/@id")
        num = 0

        #获取ID数量，并逐个下载，并给下载文件命名
        while num < len(imp):
            down_fire = code.xpath(
                "//table[@id='att_xtable_attachment']/tbody/tr/td[@class='upload_list_filename_view']/text()")
            for i in imp:#找到下载ID参数


                down_url = 'http://oa.bears.com.cn:27292/sys/attachment/sys_att_main/sysAttMain.do?method=download&fdId='+i
                res = requests.get(down_url,headers=headers,cookies=a).content

                if not os.path.exists('03.管理标准'):
                    os.mkdir('03.管理标准')

                with open('03.管理标准/%s'%down_fire[num],'wb') as g:
                    g.write(res)
                    num += 1

url = 'http://oa.bears.com.cn:27292/km/institution/km_institution_knowledge/kmInstitutio' \
      'nKnowledgeIndex.do?method=listChildren&categoryId=15dbf410dca548412ab6' \
      '4024e8bb4521&q.docStatus=30&orderby=docC' \
      'reateTime&o' \
      'rdertype=down&__seq=1599054519269&s_ajax=true'
# get_infomation(url)
webget(url)
