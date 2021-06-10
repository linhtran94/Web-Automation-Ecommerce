import csv
import operator
import time
import pytest
from selenium import webdriver

from page.SortResultPage.SortShopeePage import ShopeePage
from page.SortResultPage.SortTikiPage import TikiPage
from utilities.logger import Logger


class TestSort:
    logger = Logger.logger()

    @pytest.fixture(scope="class")
    def setup(self, request):
        driver = webdriver.Chrome(executable_path="D:\\DATA DESKTOP\\Website_Automation\\Website_Automation"
                                                  "\\chromedriver.exe")
        request.cls.driver = driver
        driver.implicitly_wait(10)
        yield driver
        driver.close()
        driver.quit()
        print('Test Completed')

    @pytest.fixture()
    def sortTiki(self, setup):
        return TikiPage(setup)

    @pytest.fixture()
    def sortShopee(self, setup):
        return ShopeePage(setup)

    # Values of Tiki page
    ip11_value = 'iPhone 11'
    listTiki = []
    listShopee = []

    # This function will implement manual test case step by step accordingly:
    #  1. Open and load URL
    #  2. Find element of Search-box > Click to Search-box
    #  3. Input 'iPhone 11' to Search-box
    #  4. Click on Search button for navigating to Product page
    #  5. Validate all results output on screen
    #  6. Print all output related to iPhone11 into CSV file
    def test_001_TIKI_search_print_output(self, sortTiki):
        listA = []
        sortTiki.load_tiki_url()
        sortTiki.click_search_box()
        sortTiki.input_to_search_box(self.ip11_value)
        sortTiki.click_search_button()
        print('Input passed')
        listA = sortTiki.print_output_tiki_to_csv()
        self.listTiki.extend(listA)
        time.sleep(3)
        print('Sorted success')

    def test_002_SHOPEE_search_print_output(self, sortShopee):
        listB = []
        sortShopee.load_shopee_url()
        sortShopee.close_ads_button()
        sortShopee.click_search_box_shopee()
        sortShopee.input_to_search_box_shopee(self.ip11_value)
        sortShopee.click_search_button_shopee()
        print('Input passed')
        listB = sortShopee.print_output_shopee_to_csv()
        self.listShopee.extend(listB)
        time.sleep(3)
        print('Sorted success')

    def test003_Print_CSV_File(self):
        totallist = []
        totallist.extend(self.listTiki)
        totallist.extend(self.listShopee)
        totallist.sort(key=operator.attrgetter('price'))
        with open('TotalReport.csv', mode='w', encoding="utf-8") as csv_file:
            fieldnames = ['Website', 'Name', 'Price', 'Link']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for ss in totallist:
                writer.writerow({'Website': ss.website, 'Name': ss.name, 'Price': ss.price, 'Link': ss.link})
