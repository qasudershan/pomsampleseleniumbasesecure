
from pages.loginprofile_page import LoginProfilePage
from pages.autogenerator_page import AutoGeneratorPage

class TestAutoGenerator:
    def test_auto_generator(self, sb, Login_fixture, logger ):
        loginprofile = LoginProfilePage()
        autogenerator = AutoGeneratorPage()

        logger.info("Step 1: Log in")
        logger.info("Step 2: Go to Auto Generator")
        loginprofile.go_to_auto_generator(sb)

        logger.info("Step 3: Select the 3rd suggested example from the Suggested dropdown.")
        autogenerator.select_3rd_example_from_the_suggested_dropdown(sb)

        logger.info("Step 4: Click Generate and wait for the process to complete.")
        autogenerator.click_generate(sb)

        logger.info("Step 5: Add the generated deck to Favorites.")
        autogenerator.add_the_generated_deck_to_favorites(sb)

        logger.info("Step 6: Download the deck/slide.")
        autogenerator.download_the_deck_slide(sb)

        logger.info("Step 7: log out via the Profile.")
        loginprofile.logout(sb)


