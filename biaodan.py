# import requests
# sessiion = requests.Session()
# params = {'username':'zhaolf','password':'password'}
# r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php',params=params)
# print(r.text)
# print('cokkies is set to :')
# print(r.cookies.get_dict())
# print('Going to profile page..')
#
# s = sessiion.get('http://pythonscraping.com/pages/cookies/profile.php')
# print(s.text)
#

from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import requests
auth = HTTPBasicAuth('sss','password')
r = requests.get('http://pythonscraping.com/pages/auth/login.php',auth=auth)
# print(r.text)
