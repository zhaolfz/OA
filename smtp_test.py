import smtplib
from email.mime.text import MIMEText
from email.header import Header
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time



mail_host = 'smtp.qq.com'
mail_user = 'zhaolfz@foxmail.com'
mail_password = 'trudtquhwwenbfgb'




From = 'zhaolfz@foxmail.com'
to = ['3511286145@qq.com']

authorization = 'trudtquhwwenbfgb'
def senemail(msg):
    try:
        msg = MIMEText('{}'.format(msg))
        smtpObj = smtplib.SMTP(mail_host,25)
        smtpObj.login(mail_user,mail_password)
        smtpObj.sendmail(From,to,msg.as_string())
        print('success')
    except smtplib.SMTPException:
        print('error.failed')

html = urlopen('https://isitchristmas.com/')
bs = BeautifulSoup(html,'html.parser')
title = bs.find('a',{'id':'answer'}).attrs['title']
a = 0
while  title == '不是':

    a += 1
    print('It is not chistmas yet,检查次数:{}'.format(a))
    time.sleep(3600)

    bs = BeautifulSoup(html,'html.parser')

senemail('It\s Chirtmas!,according to https://isitcharistams.com,it ischms')

