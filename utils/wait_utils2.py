
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class WaitUtils:

    def __init__(self,driver):

        self.driver = driver
        self.wait = WebDriverWait(driver,timeout=10)


    def wait_for_visibility(self,locator):
        self.wait.until(EC.visibility_of_element_located(locator))


    