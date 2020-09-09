# import json
# from urllib.request import urlopen
#
# def getCountry(ipadress):
#     response = urlopen("http://ip.taobao.com/service/getIpInfo.php?ip="+ipadress).read().decode('utf-8')
#     response1 = urlopen("http://ip.taobao.com/service/getIpInfo.php?ip=" + ipadress)
#     response2 = urlopen("http://ip.taobao.com/service/getIpInfo.php?ip=" + ipadress).read()
#     response3 = urlopen("http://ip.taobao.com/service/getIpInfo.php?ip=" + ipadress).read().decode('utf-8')
#     print('1',response1)
#     print('2',response2)
#     print('3',response3)
#     print('0',response)
#     responseJson = json.loads(response)
#     return responseJson.get('msg')
# print(getCountry('14.213.126.126'))


import json
jsonstring = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],' \
             '"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonobj = json.loads(jsonstring)

print(jsonobj.get('arrayOfNums'))
print(jsonobj.get('arrayOfNums')[0])
print(jsonobj.get('arrayOfNums')[0].get('number'))
print(jsonobj.get('arrayOfNums')[2].get('number'))
print(jsonobj.get('arrayOfFruits')[1].get('fruit'))
