import logging
import os
import pytest
import keyring
from pages.loginprofile_page import LoginProfilePage

@pytest.fixture(scope="function")
def logger(request):
    # Create a logger with a name based on the test function
    test_name = request.node.name
    log_folder = os.getenv("LOG_FOLDER", "logs/latest_logs")
    os.makedirs(log_folder, exist_ok=True)

    # Configure logger
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)

    # Create a file handler for the current test
    log_file = os.path.join(log_folder, f"{test_name}.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Create a console handler (optional, for terminal output)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Set formatting for handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Cleanup handlers after the test
    yield logger
    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)

@pytest.fixture(scope="function")
def Login_logout_fixture(sb, logger):

    SERVICE_NAME = "prezent_ai"
    email = keyring.get_password(SERVICE_NAME, "LOGIN_EMAIL")
    password = keyring.get_password(SERVICE_NAME, "LOGIN_PASSWORD")

    if not email or not password:
        raise ValueError("Credentials not found in Keychain. Please set them up first.")

    loginprofile = LoginProfilePage()

    logger.info("Log in initiated")
    loginprofile.login(sb, email, password)
    logger.info("Log in done")
    # yield loginprofile
    # loginprofile.logout(sb)



