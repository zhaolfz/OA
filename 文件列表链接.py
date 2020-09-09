import requests
from lxml import etree
import json
from bs4 import BeautifulSoup
url = 'http://oa.bears.com.cn:27292/km/institution/km_institution_knowledge/kmInstitut' \
      'ionKnowledge.do?method=view&fdId='+'172919f1753103f853855884b3995433'
print(url)

# url = 'http://oa.bears.com.cn:27292/km/institution/?categoryId=15dbf410dca548412ab64024e8bb4521#cri.q=docStatus:30'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

cookies = {'Cookie': 'j_lang=zh-CN; JSESSIONID=6E16932E1745472E3DC172420CED1BED; LtpaToken=AAECAzVGNTc4MUI0NU'
                     'Y1ODJBNzR6aGFvbGaxQFyg6/I8UqXwMGCxmRsqsA7M6A=='}
response = requests.get(url,headers=headers,cookies=cookies)

print(response)


# code = etree.HTML(response)
#
# info = code.xpath("//div")
#
# #//div[@class='clearfloat lui_listview_rowtable_summary_content_box']/dl[2]/dt/a/@href
# print(info)


#------
# 下载链接：http://oa.bears.com.cn:27292/sys/attachment/sys_att_main/sysAttMain.do?method=download&fdId=16a04bef01c896732066e084b8fa5385