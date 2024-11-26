class AutoGeneratorPage:
    GENERATE_BUTTON = """//span[contains(text(), "Generate")]"""
    TEXTAREA_INPUT = """//textarea"""
    SUGGESTED_3RD_EXAMPLE = """//p[@id="generate-suggested-2"]"""
    SMART_LAYOUT = """//div[@class="heading"][contains(text(), "Smart Layout")]"""
    ADD_FAVORITES = """//i[@name="favorite-icon"]"""
    ADD_TO_FAVORITES_BUTTON = """//button/span[contains(text(), "Add to Favorites")]"""
    ADDED_TO_FAVORITES_TEXT = """//span[contains(text(), "Added to Favorites")]"""
    ADD_PREZENTATION_TO_FAVORITES_CLOSE = """//div[contains(@class, 'generateActionModalContainer')]//div[contains(@class, 'closeIconContainer')]//button[contains(@class, 'mdi-close')]"""
    DOWNLOAD_ICON = """//span[@name="download-icon"]"""
    DOWNLOAD_PREZENTATION_HEADING = """//div[contains(text(), "Download Prezentation")]"""
    DOWNLOAD_BUTTON = """//button[@id="download-btn"]"""
    DOWNLOAD_AS_PPTX_OPTION = """//span[contains(text(), "Download as pptx")]"""
    DOWNLOAD_COMPLETED = """//span[contains(text(), "Download Completed")]"""

    def select_3rd_example_from_the_suggested_dropdown(self, sb):
        sb.click(self.TEXTAREA_INPUT)
        sb.click(self.SUGGESTED_3RD_EXAMPLE)

    def click_generate(self, sb):
        sb.click(self.GENERATE_BUTTON)
        sb.wait_for_element_visible(self.SMART_LAYOUT, timeout=180)

    def add_the_generated_deck_to_favorites(self, sb):
        sb.click(self.ADD_FAVORITES)
        sb.click(self.ADD_TO_FAVORITES_BUTTON)
        sb.wait_for_element_visible(self.ADDED_TO_FAVORITES_TEXT, timeout=10)
        sb.click(self.ADD_PREZENTATION_TO_FAVORITES_CLOSE)

    def download_the_deck_slide(self, sb):
        sb.click(self.DOWNLOAD_ICON)
        sb.wait_for_element_visible(self.DOWNLOAD_PREZENTATION_HEADING, timeout=5)
        sb.click(self.DOWNLOAD_BUTTON)
        sb.click(self.DOWNLOAD_AS_PPTX_OPTION)
        sb.wait_for_element_visible(self.DOWNLOAD_COMPLETED, timeout=20)












