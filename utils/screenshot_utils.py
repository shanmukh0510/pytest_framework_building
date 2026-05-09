import os
from datetime import datetime


def take_screenshot(driver, test_name):

    # Create screenshots folder if not exists
    folder = "screenshots"

    os.makedirs(folder, exist_ok=True)

    # Timestamp for unique screenshot name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Final screenshot path
    file_name = f"{test_name}_{timestamp}.png"

    path = os.path.join(folder, file_name)

    # Capture screenshot
    driver.save_screenshot(path)

    return path