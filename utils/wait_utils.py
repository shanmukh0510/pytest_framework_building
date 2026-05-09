# utils/wait_utils.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:

    def __init__(self, driver, timeout=20):

        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # =====================================================
    # Wait For Element Visibility
    # =====================================================

    def wait_for_visibility(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # =====================================================
    # Wait For Element Clickable
    # =====================================================

    def wait_for_clickable(self, locator):

        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    # =====================================================
    # Wait For Element Presence
    # =====================================================

    def wait_for_presence(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    # =====================================================
    # Wait For Title Contains
    # =====================================================

    def wait_for_title_contains(self, text):

        return self.wait.until(
            EC.title_contains(text)
        )

    # =====================================================
    # Wait For URL Contains
    # =====================================================

    def wait_for_url_contains(self, text):

        return self.wait.until(
            EC.url_contains(text)
        )

    # =====================================================
    # Wait For Invisibility
    # =====================================================

    def wait_for_invisibility(self, locator):

        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )
    



    