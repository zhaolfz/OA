import requests
from lxml import etree
import json
from bs4 import BeautifulSoup
url = 'http://oa.bears.com.cn:27292/sys/attachment/sys_att_main/sysAttMain.do?method=download&fdId=1744714b4a6ac7fe1da661c4b8f859f2'


print(url)

# url = 'http://oa.bears.com.cn:27292/km/institution/?categoryId=15dbf410dca548412ab64024e8bb4521#cri.q=docStatus:30'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

cookies = {'Cookie': 'j_lang=zh-CN; JSESSIONID=7A412515B0D214E6902E93BB1462566F; LtpaToken=AAECAzVGNjBDQTg5NUY2MTczNDl6'
                     'aGFvbGbsLr33qQQxukkOoIxIV0urDDvxxg=='}
response = requests.get(url,headers=headers,cookies=cookies)
frie_name = [1,2]
for a in frie_name:
    with open('%s.pdf'%a,'wb') as f:
        f.write(response.content)
print(response)


# code = etree.HTML(response)
#
# info = code.xpath("//div")
#
# #//div[@class='clearfloat lui_listview_rowtable_summary_content_box']/dl[2]/dt/a/@href
# print(info)


#------
# 下载链接：http://oa.bears.com.cn:27292/sys/attachment/sys_att_main/sysAttMain.do?method=download&fdId=16a04bef01c896732066e084b8fa5385