from selenium import webdriver

class DriverFactory:

    @staticmethod
    def get_driver(browser):

        browser = browser.lower()

        if browser == "chrome":
            driver = webdriver.Chrome()

        elif browser == "firefox":
            driver = webdriver.Firefox()

        elif browser == "edge":
            driver = webdriver.Edge()

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.maximize_window()
        return driver