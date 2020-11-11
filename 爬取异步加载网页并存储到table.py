import requests
from bs4 import BeautifulSoup
import json
import random
import os
import sqlite3
# import reqiests
# from lxml import etree  ---xpath
def find():
    urls = 'https://www.1905.com/api/content/index.php'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                            "(KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.3"}

    params = {'callback': 'reloadList',
                    'm': 'converged',
                    'a': 'info',
                    'type': 'jryp',
                    'year': '2020',
                    'month': '5'}
    response = requests.get(urls,headers=headers,params=params)
    html = response.text
    print('html1',html)
    html = html.replace('reloadList(','').replace(')','')
    print('html2',html)
    hh = json.loads(html)

    for i in hh['info']:
        title = i['title']
        thumb = i['thumb']
        url = i['url']
        airtime = i['airtime']
        img = requests.get(thumb).content
        img_name = random.randint(1000,9999)
        if not os.path.exists('ss'):
            os.mkdir('ss')
        with open('ss/%s.jpg'%img_name,'wb') as g:
            g.write(img)
        save_data(content=title,link=thumb,img=img_name)


# 创建表
def creat_db():
    conn = sqlite3.connect('film.db')
    # host = '127.0.0.1', port = 3306,
    # user = 'root', passwd = 'root', db = 'mysql'
    # 创建光标
    c = conn.cursor()#他就是个民工
    c.execute('CREATE TABLE filmdata(id INTEGER PRIMARY KEY AUTOINCREMENT,content text,link text,img text)')
    '''新建数据库'''
    conn.commit()
    conn.close()

# 保存爬取的数据
def save_data(content,link,img):
    conn = sqlite3.connect('film.db')
    c = conn.cursor()
    c.execute("INSERT into filmdata(content,link,img) VALUES ('{0}','{1}','{2}')".format(content,link,img))
    conn.commit()
    conn.close()
# 查看数据
def show_data():
    conn = sqlite3.connect('film.db')
    c = conn.cursor()
    res = c.execute("select * from filmdata")
    for i in res:
        print(i)

    conn.close()
if __name__ =='__main__':
    find()
    # show_data()
    # creat_db()
