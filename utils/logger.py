import logging
import os


def get_logger(name="framework"):

    # Create logs folder if not exists
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    # Avoid duplicate logs
    if not logger.handlers:

        # File Handler
        file_handler = logging.FileHandler(
            os.path.join(log_dir, "automation.log")
        )

        # Console Handler
        console_handler = logging.StreamHandler()

        # Log Format
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger