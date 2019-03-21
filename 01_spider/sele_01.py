import time
from selenium import webdriver

'''setup:
install selenium and chromedriver
sudo mv chromedriver /usr/bin
or: $PATH???
'''

d = webdriver.Chrome()
d.get('https://www.baidu.com')

time.sleep(10)
d.close()