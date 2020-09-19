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

    # url = 'http://oa.bears.com.cn:27292/km/institution/?categoryId=15dbf410dca548412ab64024e8bb4521#cri.q=docStatus:30'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

    cookies = {'Cookie': 'JSESSIONID=15272CCA16F28A3F671BFA2668B6EAE7; LtpaToken=AAECAzVGNThDQzA5NUY1OTc0Qzl6aGFv'
                         'bGb7xXvhe3IcLXRFCW4zF02jnO2SUQ==; j_lang=zh-CN'}
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
        information = {}
        inf = []
        for i in data['datas']:

            id = i[0]['value']
            title = i[2]['value']
            fdNumber = i[3]['value']
            bm = i[6]['value']
            name =i[7]['value']
            time = i[8]['value']
            name = re.findall('>.*<',name)[0].replace('<','').replace('>','')

            # print('ID:{}:文件名称:{} \n文件编号:{} 所属部门:{} 录入者：{} 生效时间:{}\n'.format(id,title,fdNumber,bm,name,time))
            #待做：将以上7个关键字段格式化，并返回信息
            information['id'] = id
            information['title'] = title
            information['fdNumber'] = fdNumber
            information['bm'] = bm
            information['name'] = name
            return information


def webget():

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

    cookies = {
        'Cookie': 'JSESSIONID=E08777C985F951DAA750AA177B700701; LtpaToken=AAECAzVGNjRCOTNCNUY2NTYxRkJ6aGFvbGaxh5iQkT/hU'
                  'QYkFBpRiM9wx4XJ8w==; j_lang=zh-CN'}
    #打开文件页面
    # for url in infomation:
    url = 'http://oa.bears.com.cn:27292/km/institution/km_institution_knowledge/kmInstitutionKnow' \
          'ledge.do?method=view&fdId=16a04be87210a0b4ae0a1ae450a9b3ea'
    #配置浏览器不打开页面，只在后台运行
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('disable-gpu')
    # chrome_options = chrome_options
    chrome = webdriver.Chrome()
    chrome.get(url)
    # print('header:',headers)
    # 输入账号密码
    name = chrome.find_element_by_name('j_username')
    password = chrome.find_element_by_name('j_password')
    name.send_keys('zhaolf')
    password.send_keys('19921231Zlf')

    # 登录
    login_button = chrome.find_element_by_class_name("lui_login_button_div_c")
    login_button.click()
    html = chrome.page_source
    code = etree.HTML(html)
    dict_id ={}
    imp = code.xpath("//table[@id='att_xtable_attachment']/tbody/tr/@id")




    # dict_id[imp] = down_fire

    # print(dict_id)
    #尝试将imp和down_fire提取到字典中
    num = 0
    while num < len(imp):
        down_fire = code.xpath(
            "//table[@id='att_xtable_attachment']/tbody/tr/td[@class='upload_list_filename_view']/text()")
        for i in imp:#找到下载ID参数


            down_url = 'http://oa.bears.com.cn:27292/sys/attachment/sys_att_main/sysAttMain.do?method=download&fdId='+i
            res = requests.get(down_url,headers=headers,cookies=cookies).content

            if not os.path.exists('03.管理标准'):
                os.mkdir('03.管理标准')

            with open('03.管理标准/%s'%down_fire[num],'wb') as g:
                g.write(res)
                num += 1

    cookies = chrome.get_cookies()  # 利用selenium原生方法得到cookies
    ret = ''
    for cookie in cookies:
        cookie_name = cookie['name']
        cookie_value = cookie['value']
        ret = ret + cookie_name + '=' + cookie_value + ';'  # ret即为最终的cookie，各cookie以“;”相隔开
        # print('ret',ret)
    headers = {
        'Host': 'oa.bears.com',
        'Referer': 'http://oa.bears.com.cn:27292/km/institution/km_institution_knowledge/kmInstitutionKnow' \
          'ledge.do?method=view&fdId=16a04be87210a0b4ae0a1ae450a9b3ea',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': ret } # 需要登陆后捕获cookie并调用



url = 'http://oa.bears.com.cn:27292/km/institution/?categor' \
      'yId=15dbf410dca548412ab64024e8bb4521#cri.q=docStatus:30'
# get_infomation(url)
webget()
a = 1