import requests
response = requests.get('http://img.ivsky.com/img/tupian/pre/202003/11/bianjing_muyangquan-008.jpg')

print(response.text)