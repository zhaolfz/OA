import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'https://tieba.baidu.com/f?kw=%E4%BD%9B%E5%B1%B1%E8%B4%B4&ie=utf-8'
html =urlopen(url)
bs4 = BeautifulSoup(html,'html.parser')

tables = bs4.findAll('li',{'class':'j_thread_list clearfix'})
# print(table)

for table in tables:
    rows = table.find_all('a',{'class':'j_th_tit'})


    csvFile = open('edidor.csv','wt+',encoding='utf-8')
    writer = csv.writer(csvFile)
    try:
        for row in rows:
            csvrow = []

            csvrow.append(row.get_text())
            print(csvrow)
            writer.writerow(csvrow)
    finally:
        csvFile.close()


# print(body.find_all('h3'))
# title =