import pytest

from pages.login_page import LoginPage
from utils.logger import get_logger
from utils.data_reader import load_json_data


logger = get_logger()


# Load JSON Data
test_data = load_json_data(
    "testdata/login_data.json"
)


@pytest.mark.parametrize("data", test_data)
def test_valid_login(driver, data):

    logger.info("Starting login test")

    login_page = LoginPage(driver)

    login_page.login(
        data["username"],
        data["password"]
    )

    logger.info("Login action completed")

    current_url = login_page.get_current_url()

    logger.info(f"Current URL: {current_url}")

    if data["username"] == "Admin":

        assert "dashboard" in current_url.lower()

    else:

        assert "auth/login" in current_url.lower()