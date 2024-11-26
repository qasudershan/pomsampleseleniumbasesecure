from pages.autogenerator_page import AutoGeneratorPage

class LoginProfilePage:
    URL = "https://prezent-uatstaging.myprezent.com/signin"
    EMAIL_INPUT = "input[id='username']"
    PASSWORD_INPUT = "input[id='password']"
    CONTINUE_BUTTON = "button[id='continue']"
    LOGIN_BUTTON = "button[id='submit']"
    BASICS_TAB = """a[href="#basics"]"""
    TEMPLATES_TAB = """a[href="#templates"]"""
    TEMPLATES_TAB_HEADER = """//*[@class="slide-settings-title"][contains(text(), "PrezentCompany Templates")]"""
    CURRENT_SELECTION_BUTTON = """//*[@id="templates"]//button[@class="v-btn v-btn--text theme--light v-size--default select-theme active"]"""
    PROFILE_ICON = """div.right-nav-item.profile-link"""
    LOGOUT_BUTTON = """div>button.edit-profile-btn.log-out-button"""
    AUTOGENERATOR_TAB = """//*[@name--auto="generate"]"""

    def login(self, sb, email, password):

        sb.open(self.URL)
        sb.type(self.EMAIL_INPUT, email)
        sb.click(self.CONTINUE_BUTTON)
        sb.type(self.PASSWORD_INPUT, password)
        sb.click(self.LOGIN_BUTTON)
        sb.find_element(self.PROFILE_ICON, timeout=20)

    def go_to_profile(self, sb):
        sb.click(self.PROFILE_ICON)

    def click_templates_tab(self, sb):
        sb.click(self.TEMPLATES_TAB)
        sb.find_element(self.CURRENT_SELECTION_BUTTON)

    def logout(self, sb):
        sb.click(self.PROFILE_ICON)
        sb.click(self.BASICS_TAB)
        sb.click(self.LOGOUT_BUTTON)
        sb.is_element_visible(self.EMAIL_INPUT)

    def go_to_auto_generator(self, sb):
        sb.click(self.AUTOGENERATOR_TAB)
        sb.is_element_visible(AutoGeneratorPage().GENERATE_BUTTON)




