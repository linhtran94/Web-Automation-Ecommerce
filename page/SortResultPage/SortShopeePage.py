import operator
import csv
import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from selenium import webdriver
from tests.SortResultTest.SortProduct import SortProduct


class ShopeePage(BasePage):
    driver = webdriver.Chrome

    # SHOPEE WEBSITE
    # Elements of SHOPEE
    url_shopee = 'https://shopee.vn/'
    close_ads_btn = (By.XPATH, '//div[@class="shopee-popup__close-btn"]')
    search_shopee_tb = (By.XPATH, '//input[@class="shopee-searchbar-input__input"]')
    search_shopee_btn = (By.XPATH, '//button[@type="button"]')

    # Global Values
    apple_iphone_11 = "Apple iPhone 11"
    mobile_iphone_11 = "Điện Thoại Apple iPhone 11"
    reduce_price = "GIẢM"

    # Step 1. Open Shopee website
    def load_shopee_url(self):
        self.driver.get(self.url_shopee)

    def close_ads_button(self):
        self.click_element(self.close_ads_btn)

    # Step 2. Click > input > search on search box
    def click_search_box_shopee(self):
        self.click_element(self.search_shopee_tb)

    def input_to_search_box_shopee(self, ip11_shopee):
        self.input_text_element(self.search_shopee_tb, ip11_shopee)

    def click_search_button_shopee(self):
        self.click_element(self.search_shopee_btn)

    # Step 3. Scan output and print to csv file
    def print_output_shopee_to_csv(self):
        list = []
        element_shopee = self.find_elements_by_css('div[data-sqe=item] a[data-sqe=link]')
        for result in element_shopee:
            info = result.text
            product_name = ""
            product_price = ""
            product_link = result.get_attribute('href')
            if info.__contains__(self.apple_iphone_11):
                # Exclude percent and reduce price
                if info.__contains__(self.reduce_price):
                    product_name = info.split("\n", 3)[2]  # get name after excluded
                    product_price_1 = info.split("\n", 4)[3]  # get first price after excluded
                    if product_price_1[1:len(product_price_1)].__contains__("."):
                        if product_price_1.__contains__("-"):
                            product_price = product_price_1[1:11]  # substring "đ"
                        else:
                            product_price = product_price_1[1:len(product_price_1)]  # substring "đ"
                    elif product_price_1.__contains__("Giảm"):
                        product_price_2 = info.split("\n", 6)[5]  # get second price if first price do not have
                        product_price = product_price_2[1:len(product_price_2)]  # substring "đ"
                    else:
                        product_price_2 = info.split("\n", 5)[4]  # get second price if first price do not have
                        product_price = product_price_2[1:len(product_price_2)]
                else:
                    product_name = info.split("\n", 1)[0]  # get name at first index
                    price_temp = info.split("\n", 2)[1]  # get first price at second index
                    product_price = price_temp[1:len(price_temp)]
                list.append(SortProduct('SHOPEE ', product_name, product_price, product_link))
            elif info.__contains__(self.mobile_iphone_11):
                # Exclude percent and reduce price
                if info.__contains__(self.reduce_price):
                    product_name = info.split("\n", 3)[2]  # get name after excluded
                    product_price_1 = info.split("\n", 4)[3]  # get first price after excluded
                    if product_price_1[1:len(product_price_1)].__contains__("."):
                        product_price = product_price_1[1:len(product_price_1)]
                    else:
                        product_price_2 = info.split("\n", 5)[4]
                        product_price = product_price_2[1:len(product_price_2)]
                else:
                    product_name = info.split("\n", 1)[0]  # get name at first index
                    price_temp = info.split("\n", 2)[1]  # get price at second index
                    product_price = price_temp[1:len(price_temp)]
                list.append(SortProduct('SHOPEE', product_name, product_price, product_link))
        list.sort(key=operator.attrgetter('price'))
        for ss in list:
            print(ss.website + "," + ss.name + "," + ss.price + "," + ss.link)
        return list
