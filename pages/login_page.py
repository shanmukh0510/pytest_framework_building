from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    username_input = (By.NAME, "username")

    password_input = (By.NAME, "password")

    login_button = (By.XPATH, "//button[@type='submit']")
    
    def login(self, username, password):

        self.enter_text(self.username_input, username)

        self.enter_text(self.password_input, password)

        self.click(self.login_button)