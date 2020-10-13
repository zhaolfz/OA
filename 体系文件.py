import requests
from bs4 import BeautifulSoup
import random
from time import sleep
import json
import re
from lxml import etree
from selenium import webdriver
import os
import time


def get_infomation(url):
    """用于获取并返回网页中各个列表的跳转链接"""

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

    cookies = {'Cookie': 'JSESSIONID=0424C9FDEB05A86898DBBA4DF45700E5; LtpaToken=AAECAzVGODVCMjk1NUY4NjVCNTV6aGFvbGZ/GD0glQVqblZ0+QuD/2hIKPVp/Q==; j_lang=zh-CN'}
    #翻页
    num = range(2,42)#上次执行到02 表单模板，41页，下次可从42开始，可以创建目录
    # num = [1]
    # num = [3,14]
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

        yield page_urls


def login_intooa(login_url,page_url):
    """模拟浏览器登录OA，并记录返回 cookies，和各个跳转页的html"""
    # 配置浏览器不打开页面，只在后台运行
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('disable-gpu')
    # chrome_options = chrome_options

    chrome = webdriver.Chrome()

    chrome.get(login_url)

    sleep(5)
    # 输入账号密码
    name = chrome.find_element_by_name('j_username')
    password = chrome.find_element_by_name('j_password')
    name.send_keys('zhaolf')
    password.send_keys('19921231Zlf')
    #
    # # 执行登录
    login_button = chrome.find_element_by_class_name("lui_login_button_div_c")
    login_button.click()
    sleep(5)
    cookies = chrome.get_cookies()  # 利用selenium原生方法得到cookies
    a = ret_cookies(cookies) #截取cookies

    zs = 0
    for url in page_url:

        chrome.get(url)
        sleep(5)
        html = chrome.page_source
        print('当前一共有{}行内容'.format(len(page_url)))
        zs += 1
        finish = len(page_url) - zs
        print('已完成{}行,剩余{}行'.format(zs, finish))
        
        yield (html,a)

def ret_cookies(cookies):
    """用于获取网页的cookies"""

    ret = ''
    a = {}
    # 捕获拼接登录所用的cookies
    for cookie in cookies:
        cookie_name = cookie['name']
        cookie_value = cookie['value']
        ret = ret + cookie_name + '=' + cookie_value + ';'  # ret即为最终的cookie，各cookie以“;”相隔开

    # 将cookies写入字典中
    a['cookies'] = '{}'.format(ret)
    return a

def webget(url):


    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
    #打开文件页面（批量获取文件页面？？？？？）
    # 引入page行链接
    login_url = 'http://oa.bears.com.cn:27292'

    #登录
    # login_intooa(login_url)

    for page_url in get_infomation(url):
        #调用login_intooa函数，进入每页页面中
        htmls = login_intooa(login_url, page_url)
        for html,a in htmls:
            code = etree.HTML(html)

            imp = code.xpath("//table[@id='att_xtable_attachment']/tbody/tr/@id")
            num = 0

            title = code.xpath("//div[@class='lui_item_txt']/text()")[2].replace("\xa0",'.')

            module = code.xpath("//div[@class='lui_item_txt']/text()")[3].replace("\xa0",'.')

            mulu = title+'/'+module
            #获取ID数量，并逐个下载，并给下载文件命名
            while num < len(imp):
                down_fire = code.xpath(
                    "//table[@id='att_xtable_attachment']/tbody/tr/td[@class='upload_list_filename_view']/text()")
                for i in imp:#找到下载ID参数


                    down_url = 'http://oa.bears.com.cn:27292/sys/attachment/sys_att_main/sysAttMain.do?method=download&fdId='+i
                    res = requests.get(down_url,headers=headers,cookies=a).content

                    if not os.path.exists(mulu):
                        os.makedirs(mulu)
                    name = down_fire[num]
                    with open('{}/{}'.format(mulu,name),'wb') as g:#('03.管理标准/%s'%down_fire[num],'wb')
                        g.write(res)
                        num += 1

url = 'http://oa.bears.com.cn:27292/km/institution/km_institution_knowledge/kmInstitutionKnowledgeIndex.do?method=listChildren&categoryId=161db6003b19e718956d5894b8982583&q.docStatus=30&orderby=docCreateTime&ordertype=down&__seq=1602598601288&s_ajax=true'
# url1 = 'http://oa.bears.com.cn:27292/km/institution/km_institution_knowledge/kmInstitutionKnowledgeIndex.do?method=listChildren&categoryId=15dbf410dca548412ab64024e8bb4521&q.docStatus=30&orderby=docCreateTime&ordertype=down&__seq=1602391060620&s_ajax=true'
# url2 = 'http://oa.bears.com.cn:27292/km/institution/km_institution_knowledge/kmInstitutionKnowledgeIndex.do?method=listChildren&categoryId=15dbf410dca548412ab64024e8bb4521&q.docStatus=30&q.s_raq=0.6489840490861063&pageno=2&rowsize=15&orderby=docCreateTime&ordertype=down&s_ajax=true'
# login_url = 'http://oa.bears.com.cn:27292/login.jsp'
# page_url = 'http://oa.bears.com.cn:27292/km/institution/km_institution_knowledge/kmInstitutionKnowledgeIndex.do?method=listChildren&categoryId=15dbf410dca548412ab64024e8bb4521&q.docStatus=30&q.s_raq=0.7907000150131513&pageno=2&rowsize=15&orderby=docCreateTime&ordertype=down&s_ajax=true'
# get_infomation(url2)
webget(url)

# login_intooa(login_url,page_url)

