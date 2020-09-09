from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
import os


downloadDirectory = 'download'
baseUrl = 'http://pythonscraping.com'

def getAbsoluteURL(baseUrl,source):
    jpg = '.jpg'
    if  jpg in source:
        url = source

    else:
        return None

    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl,fileUrl,downloadDirectory):
    path = fileUrl.replace('www.','')
    path = path.replace(baseUrl,'')
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen('http://pythonscraping.com')
bs = BeautifulSoup(html,'html.parser')
downloadList = bs.findAll(src=True)

for dowload in downloadList:


    fileUrl = getAbsoluteURL(baseUrl,dowload['src'])
    if fileUrl is not None:

        urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))


