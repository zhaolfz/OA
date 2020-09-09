# class Readcsv:
#     from urllib.request import urlopen
#     from bs4 import BeautifulSoup
#     import csv
#     from io import StringIO
#     #创建csv对象
#     csvpage = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv ')
#     # 将编译后的csvpage赋值给变量data
#     data = csvpage.read().decode('ascii','ignore')
#     #在内存中读取的data赋值到file
#     dataFile = StringIO(data)
#     #用dataFile调用csv中的方法Dict，并将其返回值赋值给reader
#     dictReader = csv.DictReader(dataFile)
#     print(dictReader.fieldnames)
#     for row in dictReader:
#
#         print('The album "'+row['Name']+'" was released in ' +str(row['Year']))


# class pdfread():
#     from urllib.request import urlopen
#     from pdfminer.pdfinterp import PDFResourceManager,process_pdf
#     from pdfminer.converter import TextConverter
#     from pdfminer.layout import LAParams
#     from io import StringIO
#     from io import open
#
#     def readPDF(pdfFile):
#         rsrcmgr = PDFResourceManager()
#         retstr = StringIO()
#         laparams = LAParams()
#         divice = TextConverter(rsrcmgr,retstr,laparams=laparams)
#         process_pdf(retstr,divice,pdfFile)
#         divice.close()
#
#         content = retstr.getvalue()
#         retstr.close()
#         return content
#
#     pdfFile = open('aaa.pdf','rb')
#
#
#
#     outputString = readPDF(pdfFile)
#     print(outputString)
#     pdfFile.close()

#读取word文档
# from zipfile import ZipFile
# from urllib.request import urlopen
# from io import BytesIO
# from bs4 import BeautifulSoup
# wordFile = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
#
# #读成二进制文件
# wordFile = BytesIO(wordFile)
#
# document = ZipFile(wordFile)
#
# xml_content = document.read('word/document.xml')
#
# word_obj = BeautifulSoup(xml_content.decode('utf-8'),'xml')
#
# text_string = word_obj.findAll('w:t')
# for tex in text_string:
#     style =tex.parent.parent.find('w:pStyle')
#     if style is not None and style['w:val']=='Title':
#         print("Title is :{}".format(tex.text))
#     else:print(tex.text)
# print(xml_content.decode('utf-8'))

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter
def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace)
                for word in sentence]
    sentence = [word for word in sentence if len(word)> 1
                or (word.lower()=='a' or word.lower()=='i')]
    return sentence
def cleanInput(content):
    content = content.upper()
    content = re.sub('n','',content)
    content = bytes(content,'UTF-8')
    content = content.decode('ascii','ignore')
    sentences = content.split('.')
    return [cleanSentence(sentence) for sentence in sentences]

def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output
def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = Counter()
    ngrams_list = []
    for sentence in content:
        newNgrams = [' '.join(ngram) for ngram in
        getNgramsFromSentence(sentence, 2)]
        ngrams_list.extend(newNgrams)
        ngrams.update(newNgrams)
    return(ngrams)


content = str(
urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt')
.read(), 'utf-8')
ngrams = getNgrams(content, 2)
print(ngrams)