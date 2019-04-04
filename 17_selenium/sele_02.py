# when: 2019/04/03 9:58 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. 目前还没想好可以用这个来做什么。模拟登录？？？稍后在尝试吧。

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



d = webdriver.Chrome()
d.get('https://www.163.com/')

#
# input_box = d.find_element_by_id('ac-gn-link-search')
# input_box.click()
# real_input = d.find_element_by_id('ac-gn-searchform-input')
#
# real_input.send_keys('imac')
# real_input.send_keys(Keys.ENTER)
#
# wait = WebDriverWait(d, 10)     # not time.sleep()
# wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
# # 上面这行等价于 find_element_by_id('content_left')， 更加灵活


print(d.current_url)    # 666
print(d.get_cookies())  # 6666666666
# print(d.page_source)

# 滚动屏幕, 如何控制滚动的速度呢。。。
d.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# d.execute_script("alert('Bottom')")

# d.close()


