# when: 2019/04/03 9:54 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com


'''setup:
install selenium and chromedriver
sudo mv chromedriver /usr/bin
or: $PATH???

find_element_by_id('kw')
find_elements_by_id('kw')   # 多一个 s
P 260
'''

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


d = webdriver.Chrome()
d.get('https://www.baidu.com')
input_box = d.find_element_by_id('kw')


input_box.send_keys('apple')
input_box.send_keys(Keys.ENTER)

wait = WebDriverWait(d, 20)     # not time.sleep()
wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
# 上面这行等价于 find_element_by_id('content_left')， 更加灵活

print(d.current_url)    # 666
print(d.get_cookies())  # 6666666666
# print(d.page_source)

# 滚动屏幕
d.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# d.execute_script("alert('Bottom')")

d.close()

