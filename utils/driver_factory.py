from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class DriverFactory:

    @staticmethod
    def get_driver(browser, headless=False):

        browser = browser.lower()

        if browser == "chrome":

            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")

            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":

            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            driver = webdriver.Firefox(options=options)

        elif browser == "edge":

            options = EdgeOptions()

            if headless:
                options.add_argument("--headless=new")

            driver = webdriver.Edge(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # Maximize only for local execution
        if not headless:
            driver.maximize_window()

        return driver