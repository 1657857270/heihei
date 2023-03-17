from selenium.webdriver import Chrome
import time
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = 'https://passport.ctrip.com/user/login?backurl=https%3A%2F%2Fhotels.ctrip.com%2Fhotels%2F6542110.html%23ctm_ref%3Dhp_htl_pt_pro_01'
option = Options()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=option)
web.get(url)
time.sleep(2)
# web.implicitly_wait()
#
# # 显示等待
# el = WebDriverWait(web, 10, 0.5).until(  # until 结束等待的条件
#     EC.presence_of_element_located(By.XPATH, '//*[@id="npwd"]')
# )

web.find_element(By.XPATH, r'//*[@id="nloginname"]').send_keys("15534217839")
web.find_element(By.XPATH, r'//*[@id="npwd"]').send_keys("a15534217839")
web.find_element(By.XPATH, r'//*[@id="normalview"]/form/p/input').click()
web.find_element(By.XPATH, r'//*[@id="nsubmit"]').click()
time.sleep(3)
page_source = web.page_source
tree = etree.HTML(page_source)
title = tree.xpath('//*[@id="ibu-hotel-detail-head"]/div[1]/div[1]/div[1]/h1/text()')
comments = tree.xpath('//*[@class="comment"]/p/text()')
print(title)
print(comments)
