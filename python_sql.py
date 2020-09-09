from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import pymysql
#创建连接对象
conn = pymysql.connect(host='127.0.0.1',port=3306,
                       user='root',passwd='root',db='mysql')
# 创建光标对象、用于执行sql语句
cur = conn.cursor()
cur.execute('USE scraping')
random.seed(datetime.datetime.now())

def store(title):
    # print(title)
    cur.execute('insert into pages (title) value (%s)',title)

    cur.connection.commit()
def getlinks():
    html = urlopen('https://www.hao123.com/?tn=48020221_28_hao_pg')
    bs = BeautifulSoup(html,'html.parser')
    title = bs.find('div',{'id':'indexLogo'}).find('a',{'class':'hao123logourl'}).attrs['title']
    # print(title)
    # content = bs.find('div',{'id':'mw-content-text'}).find(   'p').get_text()
    store(title)
    # return bs.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))

getlinks()
# try:
#     while len(links)>0:
#         newArticle = links[random.randint(0,len(links)-1)].attrs['href']
#         print(newArticle)
#         links = getlinks(newArticle)

cur.close()
conn.close()
