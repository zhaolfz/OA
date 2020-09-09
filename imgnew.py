# from selenium import webdriver
# import time
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.common.exceptions import StaleElementReferenceException
#
# def wait(driver):
#     elem = driver.find_element_by_tag_name("html")
#     count = 0
#     while True:
#         count += 1
#         if count >20 :
#             print('timing out after 10 second and returning')
#             return
#         time.sleep(5)
#         try:
#             elem == driver.find_element_by_tag_name('html')
#         except StaleElementReferenceException:
#             return
# driver = webdriver.PhantomJS(executable_path=r'D:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs')
# driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')
# wait(driver)
# print(driver.page_source)







from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

#用ph的地址参数调用webdiver中的ph方法，也是创建一个无头浏览器对象
divers = webdriver.PhantomJS(executable_path=r'D:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs')
divers.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')
try:
    body = WebDriverWait(divers,15).until(ec.presence_of_element_located((By.XPATH,"//body[contains(text(),'This is the page you are looking for!')]")))
    print(body.text)
except TimeoutException:
    print('time out')