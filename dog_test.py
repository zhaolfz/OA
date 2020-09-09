from bs4 import BeautifulSoup
import requests
import os
import re


def gethtml(urls, title, img_num):
    for url in urls:
        response = requests.get(urls)
        html = response.text
        bs = BeautifulSoup(html, 'html.parser')
        img_addres = bs.find('img', {'id': 'imgis'}).attrs.get('src')
        fire_name = img_addres.split('/')[-1]
        rel_addres = 'http:' + img_addres
        # 获取真实图片响应
        response = requests.get(rel_addres)
        dir_name = title.strip()

        num = int(img_num[0])

        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        a = 0
        while a < num:
            path = dir_name + '/' + fire_name
            with open(path, 'wb') as dog:
                dog.write(response.content)
                a += 1
            print('已完成{}张图片下载,还剩{}张图片'.format(a, num - a))


def getimg(start_url):
    response = requests.get(start_url)
    html = response.text
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('div', {'class': 'al_tit'}).find('h1').text
    print(title)
    img_num = re.findall('\d+', title)
    urls = []
    body = bs.find_all('div', {'class': 'il_img'})
    for line in body:

        line = str(line)
        url = re.findall('/.*[h][t][m][l]', line)
        real_url = 'https://www.ivsky.com'+ str(url[0])

        urls.append(real_url)


        # return urls,title,img_num


url = 'https://www.ivsky.com/bizhi/dilireba_v58838/'
urls = getimg(url)
title = urls
print(title)


# 需解决重复报进度的问题






