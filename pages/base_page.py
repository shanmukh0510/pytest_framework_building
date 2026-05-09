from utils.wait_utils import WaitUtils
from selenium import webdriver

class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WaitUtils(driver)

    # =====================================================
    # Click Element
    # =====================================================

    def click(self, locator):

        element = self.wait.wait_for_clickable(locator)

        element.click()

    # =====================================================
    # Enter Text
    # =====================================================

    def enter_text(self, locator, text):

        element = self.wait.wait_for_visibility(locator)

        element.clear()

        element.send_keys(text)

    # =====================================================
    # Get Text
    # =====================================================

    def get_text(self, locator):

        element = self.wait.wait_for_visibility(locator)

        return element.text

    # =====================================================
    # Check Element Displayed
    # =====================================================

    def is_displayed(self, locator):

        element = self.wait.wait_for_visibility(locator)

        return element.is_displayed()

    # =====================================================
    # Get Page Title
    # =====================================================

    def get_title(self):

        return self.driver.title

    # =====================================================
    # Get Current URL
    # =====================================================

    def get_current_url(self):

        return self.driver.current_url