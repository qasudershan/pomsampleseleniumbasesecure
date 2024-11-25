# import logging
# import pytest
#
from pages.loginprofile_page import LoginProfilePage
from pages.templates_page import TemplatesPage
from pages.fingerprint_page import FingerPrintPage
# from tests.base_test import BaseTest
#
# logger = logging.getLogger(__name__)

class TestFingerPrint:

    def test_finger_print(self, Login_logout_fixture, logger, sb):
        loginprofile = LoginProfilePage()
        templates = TemplatesPage()
        fingerprint = FingerPrintPage()

        logger.info("Step 1: Log in")
        logger.info("Step 2: Navigate to profile")
        loginprofile.go_to_profile(sb)

        logger.info("Step 3: Click fingerprint tab")
        fingerprint.go_to_fingerprint_tab(sb)

        logger.info("Step 4: Click on Re-take Fingerprint and complete the steps.")
        fingerprint.retake_fingerprint(sb)
        # fingerprint.click_discover_my_fingerprint(sb)
        fingerprint.build_communication_fingerprint(sb)

        logger.info("Step 5: Click Go Back to Prezent and then go to Profile and log out.")
        fingerprint.go_back_to_prezent(sb)

        logger.info("*********Test Successful*************")
