import operator

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from selenium import webdriver
from tests.SortResultTest.SortProduct import SortProduct


class TikiPage(BasePage):
    driver = webdriver.Chrome

    # TIKI WEBSITE
    # Elements of TIKI
    url_tiki = 'https://tiki.vn/'
    input_tiki_tb = (By.XPATH, '//input[@data-view-id="main_search_form_input"]')
    search_tiki_btn = (By.XPATH, '//button[@data-view-id="main_search_form_button"]')

    # Global Values
    mobile_iphone_11 = "Điện Thoại iPhone 11"
    is_freeship = "Freeship"

    # Step 1. Open Tiki website
    def load_tiki_url(self):
        self.driver.get(self.url_tiki)

    # Step 2. Click > input > search on search box
    def click_search_box(self):
        self.click_element(self.input_tiki_tb)

    def input_to_search_box(self, ip11_value):
        self.input_text_element(self.input_tiki_tb, ip11_value)
        self.wait_elements()

    def click_search_button(self):
        self.click_element(self.search_tiki_btn)
        self.wait_elements()

    # Step 3. Scan output and print to csv file
    def print_output_tiki_to_csv(self):
        # 3a. Scan and validate output:
        list = []
        element_tiki = self.find_elements_by_css('a.product-item')
        for info in element_tiki:
            info_e = info.text
            product_name = ""
            product_price = ""
            product_link = ""
            if info_e.__contains__(self.mobile_iphone_11):
                if info_e.split("\n", 1)[0].__contains__(self.is_freeship):  # is Free Ship
                    product_link = info.get_attribute('href')
                    product_name = info_e.split("\n", 2)[1]  # Exclude Freeship
                    if product_name.__contains__(self.mobile_iphone_11):
                        check_price_1 = info_e.split("\n", 3)[2]  # Rating/Price
                        check_price_2 = info_e.split("\n", 4)[3]  # Price
                        if check_price_1[:len(check_price_1) - 1].__contains__("."):
                            product_price = check_price_1[:len(check_price_1) - 1]
                        else:
                            product_price = check_price_2[:len(check_price_2) - 1]
                else:
                    product_link = info.get_attribute('href')
                    product_name = info_e.split("\n", 1)[0]  # Name Product
                    if product_name.__contains__(self.mobile_iphone_11):  # is not Free Ship
                        check_price_1 = info_e.split("\n", 2)[1]  # Rating/Price
                        check_price_2 = info_e.split("\n", 3)[2]  # Price
                        if check_price_1[:len(check_price_1) - 1].__contains__("."):
                            product_price = check_price_1[:len(check_price_1) - 1]
                        else:
                            product_price = check_price_2[:len(check_price_2) - 1]
                list.append(SortProduct('TIKI', product_name, product_price, product_link))
        list.sort(key=operator.attrgetter('price'))
        for ss in list:
            print(ss.website + "," + ss.name + "," + ss.price + "," + ss.link)
        return list
