import os
import keyring
from pages.loginprofile_page import LoginProfilePage
from pages.templates_page import TemplatesPage

class TestLoginProfile:

    def test_login_and_fetch_templates(self, sb, logger):

        loginprofile = LoginProfilePage()
        templates = TemplatesPage()

        SERVICE_NAME = "prezent_ai"
        email = keyring.get_password(SERVICE_NAME, "LOGIN_EMAIL")
        password = keyring.get_password(SERVICE_NAME, "LOGIN_PASSWORD")

        if not email or not password:
            raise ValueError("Credentials not found in Keychain. Please set them up first.")

        logger.info("Step 1: Log in")
        loginprofile.login(sb, email, password)
        logger.info("Logged in successfully.")

        logger.info("Step 2: Navigate to profile")
        loginprofile.go_to_profile(sb)

        logger.info("Step 3: Fetching first five templates")
        loginprofile.click_templates_tab(sb)
        template_names = templates.get_5template_names(sb)
        logger.info(f"First five templates: {template_names}")
        assert len(template_names) == 5, "The count of templates should be 5"

        logger.info("Step 4: Fetch the active template")
        active_template = templates.get_active_template(sb)
        logger.info(f"Active template: {active_template}")

        logger.info("Step 5: Log out")
        loginprofile.logout(sb)
        logger.info("**********Test completed successfully.***********")
