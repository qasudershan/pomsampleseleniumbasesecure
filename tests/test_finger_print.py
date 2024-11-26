from pages.loginprofile_page import LoginProfilePage
from pages.templates_page import TemplatesPage
from pages.fingerprint_page import FingerPrintPage

class TestFingerPrint:

    def test_finger_print(self, sb, Login_fixture, logger):
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
        fingerprint.build_communication_fingerprint(sb, logger)

        logger.info("Step 5: Click Go Back to Prezent and then go to Profile and log out.")
        fingerprint.go_back_to_prezent(sb)

        logger.info("Step 6: log out via the Profile.")
        loginprofile.logout(sb)
