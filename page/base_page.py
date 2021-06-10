from selenium.common.exceptions import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():

    # Constructor
    def __init__(self, driver):
        # BasePage class has 1 'driver' attribute
        self.driver = driver

    # Check element visibility
    def check_element_visibility(self, locator):
        try:
            WebDriverWait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutError:
            print("\n Element not found within given time")
            return False

    # Click on element
    def click_element(self, locator):
        WebDriverWait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator)).click()

    # Input text
    def input_text_element(self, locator, text):
        WebDriverWait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    # Get the text of element
    def get_text_element(self, locator):
        return WebDriverWait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator)).text

    # Switch BROWSER tab | number [0] - first tab
    def switch_browser_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])

    # Get current URL
    def get_current_url(self):
        return self.driver.current_url

    # Find elements by CSS
    def find_elements_by_css(self, css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)

    # Get current page title
    def get_page_title(self):
        return self.driver.title

    # Hover to element
    def hover_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    # Alert
    def alert_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def alert_dismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def alert_get_text(self):
        alert = self.driver.switch_to.alert
        alert.text()

    # Get the text of element
    def get_all_elements(self, locators):
        return WebDriverWait(self.driver, timeout=10).until(ec.visibility_of_all_elements_located(locators))

    # Count elements
    def count_elements(self, locators):
        return len(WebDriverWait(self.driver, timeout=10).until(ec.visibility_of_all_elements_located(locators)))

    # Wait
    def wait_elements(self):
        return self.driver.implicitly_wait(10)
