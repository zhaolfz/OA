from bs4 import BeautifulSoup
import requests
import os
import re
def gethtml(urls,title):
    # num = int(len(urls))
    a = 0
    for url in urls:
        response = requests.get(url)
        html = response.text
        bs = BeautifulSoup(html,'html.parser')
        img_addres = bs.find('img',{'id':'imgis'}).attrs.get('src')
        fire_name = img_addres.split('/')[-1]
        rel_addres = 'http:'+img_addres
    #获取真实图片响应
        response = requests.get(rel_addres)
        dir_name = title.strip()
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        if a < len(urls):
            path = dir_name+'/'+fire_name
            a += 1
            print('总计{}张图片，已完成{}张图片'.format(len(urls),a))
            with open(path,'wb') as dog:
                dog.write(response.content)
        else:
            print('无图')

def getimg(start_url):
    response = requests.get(start_url)
    html = response.text
    bs = BeautifulSoup(html,'html.parser')
    title = bs.find('div',{'class':'al_tit'}).find('h1').text

    # img_num = re.findall('\d+',title)
    urls = []
    body = bs.find_all('div',{'class':'il_img'})
    for line in body:
        line = str(line)
        url = re.findall('/.*[h][t][m][l]',line)
        urls.append('https://www.ivsky.com'+ url[0])

    return urls,title
        # gethtml(urls,title,img_num)
url = 'https://www.ivsky.com/tupian/baiqun_changfa_meinv_v59671/'
urls = getimg(url)
title = urls[1]
urls = urls[0]
gethtml(urls,title)


#需解决重复报进度的问题






