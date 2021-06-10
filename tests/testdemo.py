import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\DATA DESKTOP\\Website_Automation\\"
                                          "Website_Automation\\chromedriver.exe")

ip11_value = 'iPhone 11'

driver.get('https://shopee.vn/')
driver.find_element_by_css_selector('div.shopee-popup__close-btn').click()
time.sleep(4)
driver.find_element_by_xpath('//input[@class="shopee-searchbar-input__input"]').send_keys(ip11_value)
time.sleep(4)
driver.find_element_by_xpath('//button[@type="button"]').click()
time.sleep(2)