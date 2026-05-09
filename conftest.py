# conftest.py

import pytest

from config.config_reader import ConfigReader
from utils.driver_factory import DriverFactory
from utils.logger import get_logger
from utils.screenshot_utils import take_screenshot


# =========================================================
# LOGGER
# =========================================================

logger = get_logger()


# =========================================================
# COMMAND LINE OPTIONS
# =========================================================

def pytest_addoption(parser):

    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment name: dev/qa/prod"
    )

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name: chrome/firefox/edge"
    )


# =========================================================
# CONFIG FIXTURE
# =========================================================

@pytest.fixture(scope="session")
def config(request):

    env = request.config.getoption("--env")

    logger.info(f"Running tests on environment: {env}")

    return ConfigReader(env)


# =========================================================
# DRIVER FIXTURE (SETUP + TEARDOWN)
# =========================================================

@pytest.fixture(scope="function")
def driver(request, config):

    browser = request.config.getoption("--browser")

    logger.info(f"Launching browser: {browser}")

    # ---------------- SETUP ----------------

    driver = DriverFactory.get_driver(browser)

    driver.maximize_window()

    driver.get(config.get("base_url"))

    logger.info(f"Opened URL: {config.get('base_url')}")

    yield driver

    # ---------------- TEARDOWN ----------------

    logger.info("Closing browser")

    driver.quit()


# =========================================================
# HOOK : SCREENSHOT ON FAILURE
# =========================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Only for actual test failure
    if report.when == "call" and report.failed:

        logger.error(f"Test Failed: {item.name}")

        driver = item.funcargs.get("driver")

        if driver:

            screenshot_path = take_screenshot(driver, item.name)

            logger.info(f"Screenshot saved at: {screenshot_path}")


# =========================================================
# SESSION START
# =========================================================

def pytest_sessionstart(session):

    logger.info("========== TEST EXECUTION STARTED ==========")


# =========================================================
# SESSION FINISH
# =========================================================

def pytest_sessionfinish(session, exitstatus):

    logger.info("========== TEST EXECUTION COMPLETED ==========")