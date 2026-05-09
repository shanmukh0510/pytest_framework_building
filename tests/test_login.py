# from pages.login_page import LoginPage
# from utils.logger import get_logger
# from pages.base_page import BasePage



# logger = get_logger()


# def test_valid_login(driver):

#     logger.info("Starting login test")

#     login_page = LoginPage(driver)
#     base_page = BasePage(driver)

#     login_page.login(
#         "Admin",
#         "admin123"
#     )

#     logger.info("Login successful")

#     title = base_page.get_title()

#     print(title)

#     assert "opensource-demo.orangehrmlive" in driver.current_url



    # tests/test_login.py

from pages.login_page import LoginPage
from utils.logger import get_logger


logger = get_logger()


def test_valid_login(driver, config):

    logger.info("Starting login test")

    login_page = LoginPage(driver)

    # =====================================================
    # Login
    # =====================================================

    login_page.login(
        config.get("username"),
        config.get("password")
    )

    logger.info("Login successful")

    # =====================================================
    # Validation
    # =====================================================

    current_url = login_page.get_current_url()

    logger.info(f"Current URL: {current_url}")

    page_title = login_page.get_title()

    logger.info(f"Page Title: {page_title}")

    assert "dashboard" in current_url.lower(), \
        "Login failed - Dashboard URL not found"

    logger.info("Login validation successful")