import time
from seleniumbase.common.exceptions import NoSuchElementException

class FingerPrintPage:
    FINGERPRINT_TAB = """a[href="#fingerprint"]"""
    RETAKE_FINGERPRINT_LINK = """//*[@class="btn-retake"]"""
    DISCOVER_MY_FINGERPRINT_BUTTON = """#discover"""
    back_button = """div.back-button"""
    MY_FINGERPRINT_HEADER = """//*[@class="question-header"]"""
    # MY_FINGERPRINT_QUESTION_INTENT = """//*[@class="question-content-header"]/div/p"""
    MY_FINGERPRINT_QUESTION_INTENT = """//*[@class="question-content-header"]"""

    MY_FINGERPRINT_QUESTION_INTENT_OPTION = """.card-item"""
    MY_FINGERPRINT_QUESTION_INTENT_OPTION_FIRST = """.card-item:nth-child(1)""" #############

    SELECT_FROM_COMMON_PREFERENCES_HEADER = """//div[@class="header"][contains(text(), "from common")]"""
    SELECTION_TITLE_FOR_MULTIPLE_SELECTION = """//*[@class="selection-title"]"""
    NEXT_BUTTON_DISABLED = """//button[@disabled]/span[contains(text(), "Next")]"""
    NEXT_BUTTON = """//span[contains(text(), "Next")]"""

    SELECTION_ITEM_FOR_ONE_SELECTION = """//*[@class="cards-wrapper"]//div[@class="item-name"]"""
    SELECTION_ITEM_INDUSTRY_FOR_ONE_SELECTION = """//*[@class="cards-wrapper industry"]//div[@class="item-name"]"""

    SELECTION_GROUP_FOR_MULTIPLE_SELECTION = """//*[@class="selection group-items"]//span[@class="selection-title"]"""

    SELECTION_ITEM_FOR_MULTIPLE_SELECTION = """//*[@class="cards-wrapper"]//div[@class="item-name"]"""

    JOB_TITLE_HEADER = """//div[@class="header"][contains(text(), "job title")]"""
    JOB_TITLE_DROP_DOWN = """//div/div/input[@placeholder="Job Title"]"""
    JOB_TITLE_DROP_DOWN_ITEM = """//div[3]/div[@class="v-list-item__content"]"""

    #Condition
    ENTER_THE_WORK_EMAILS_OF_COLLEAGUES_HEADER = """//*[@class="encourage-sub-title"][contains(text(), " Enter the work emails of colleagues you would like to invite to Prezent ")]"""
    coullegue_first_name_input = """//input[contains(@id, "name-input")]"""
    coullegue_last_name_input = """//input[contains(@id, "lastname-input")]"""
    coullegue_email_input = """//input[contains(@id, "email-input")]"""

    VIEW_MY_FINGERPRINT_BUTTON = """//button/span[contains(text(), "View my fingerprint")]"""

    RETAKE_FINGERPRINT_TEST_LINK = """//*[@class="fingerprint-center-item"]"""

    BACK_TO_PREZENT_BUTTON = """//button/span[contains(text(), "Back to Prezent")]"""


    def go_to_fingerprint_tab(self, sb):
        sb.click(self.FINGERPRINT_TAB)
        sb.find_element(self.RETAKE_FINGERPRINT_LINK)
    def retake_fingerprint(self, sb):
        sb.click(self.RETAKE_FINGERPRINT_LINK)
        sb.find_element(self.DISCOVER_MY_FINGERPRINT_BUTTON)
    def click_discover_my_fingerprint(self, sb):
        sb.click(self.DISCOVER_MY_FINGERPRINT_BUTTON)
    def get_my_fingerprint_question_intent_text(self, sb):
        return sb.get_text(self.MY_FINGERPRINT_QUESTION_INTENT)
    def get_count_my_fingerprint_question_intent_option(self, sb):
        return len(sb.find_elements(self.MY_FINGERPRINT_QUESTION_INTENT_OPTION))
    def click_my_fingerprint_question_intent_option_First(self, sb):
        count = self.get_count_my_fingerprint_question_intent_option(sb)
        import random
        i = random.randint(1, count)
        sb.click(self.MY_FINGERPRINT_QUESTION_INTENT_OPTION + ":nth-child(" + str(i) + ")")
    def get_selection_title_for_multiple_selection_text(self, sb):
        selection_title_elements = sb.find_elements(self.SELECTION_TITLE_FOR_MULTIPLE_SELECTION)
        return [template.text for template in selection_title_elements]
    def select_selection_title(self, sb):
        selection_title_list = self.get_selection_title_text(sb)
        selection_title_count = len(selection_title_list)
        sewlected_values = []
        import random
        figure = random.randint(1, selection_title_count)
        for i in range(figure):
            name = selection_title_list.pop(selection_title_list.index(random.choice(selection_title_list)))
            sewlected_values.append(name)
        return sewlected_values

    def is_element_not_present(self, sb, locator):
        try:
            sb.find_element(locator, timeout=1)
            return False  # Element is present
        except Exception:
            return True  # Element is not present

    def is_element_present(self, sb, locator):
        try:
            sb.find_element(locator, timeout=10)
            return True  # Element is present
        except NoSuchElementException:
            return False

    def build_communication_fingerprint(self, sb, logger):
        selected_item = {}
        sb.click(self.DISCOVER_MY_FINGERPRINT_BUTTON)

        while self.is_element_present(sb, self.MY_FINGERPRINT_QUESTION_INTENT) and self.is_element_not_present(sb, self.NEXT_BUTTON_DISABLED):
            temp_q = sb.find_elements(self.MY_FINGERPRINT_QUESTION_INTENT)
            temp_q_text = [template.text for template in temp_q]
            delimiter = " "
            initial_question_text = delimiter.join(temp_q_text)

            count_selection_items = len(sb.find_elements(self.MY_FINGERPRINT_QUESTION_INTENT_OPTION))

            #data capture
            selected_item[initial_question_text] = count_selection_items
            if count_selection_items > 0:
                sb.click(self.MY_FINGERPRINT_QUESTION_INTENT_OPTION_FIRST)

        while self.is_element_present(sb, self.NEXT_BUTTON_DISABLED) and self.is_element_not_present(sb, self.JOB_TITLE_HEADER):
            temp_q = sb.find_elements(self.MY_FINGERPRINT_QUESTION_INTENT)
            temp_q_text = [template.text for template in temp_q]
            delimiter = " "
            initial_question_text = delimiter.join(temp_q_text)

            if self.is_element_present(sb, self.SELECTION_TITLE_FOR_MULTIPLE_SELECTION):
                temp_selection_items = sb.find_elements(self.SELECTION_TITLE_FOR_MULTIPLE_SELECTION)
                temp_selection_items_text = [template.text for template in temp_selection_items]
                count_selection_items = len(temp_selection_items)

                # data capture
                selected_item[initial_question_text] = temp_selection_items_text
                if count_selection_items > 0:
                    sb.click(self.SELECTION_TITLE_FOR_MULTIPLE_SELECTION)
                    sb.click(self.NEXT_BUTTON)

            elif self.is_element_present(sb, self.SELECTION_ITEM_FOR_ONE_SELECTION):
                temp_selection_items = sb.find_elements(self.SELECTION_ITEM_FOR_ONE_SELECTION)
                temp_selection_items_text = [template.text for template in temp_selection_items]
                count_selection_items = len(temp_selection_items)

                # data capture
                selected_item[initial_question_text] = temp_selection_items_text
                if count_selection_items > 0:
                    sb.click(self.SELECTION_ITEM_FOR_ONE_SELECTION)
                    sb.click(self.NEXT_BUTTON)

            elif self.is_element_present(sb, self.SELECTION_ITEM_INDUSTRY_FOR_ONE_SELECTION):
                temp_selection_items = sb.find_elements(self.SELECTION_ITEM_INDUSTRY_FOR_ONE_SELECTION)
                temp_selection_items_text = [template.text for template in temp_selection_items]
                count_selection_items = len(temp_selection_items)

                # data capture
                selected_item[initial_question_text] = temp_selection_items_text
                if count_selection_items > 0:
                    sb.click(self.SELECTION_ITEM_INDUSTRY_FOR_ONE_SELECTION)
                    sb.click(self.NEXT_BUTTON)

            elif self.is_element_present(sb, self.SELECTION_GROUP_FOR_MULTIPLE_SELECTION):
                temp_selection_items = sb.find_elements(self.SELECTION_GROUP_FOR_MULTIPLE_SELECTION)
                temp_selection_items_text = [template.text for template in temp_selection_items]
                count_selection_items = len(temp_selection_items)

                # data capture
                selected_item[initial_question_text] = temp_selection_items_text
                if count_selection_items > 0:
                    sb.click(self.SELECTION_GROUP_FOR_MULTIPLE_SELECTION)
                    sb.click(self.NEXT_BUTTON)

            elif self.is_element_present(sb, self.SELECTION_ITEM_FOR_MULTIPLE_SELECTION):
                temp_selection_items = sb.find_elements(self.SELECTION_ITEM_FOR_MULTIPLE_SELECTION)
                temp_selection_items_text = [template.text for template in temp_selection_items]
                count_selection_items = len(temp_selection_items)

                # data capture
                selected_item[initial_question_text] = temp_selection_items_text
                if count_selection_items > 0:
                    sb.click(self.SELECTION_ITEM_FOR_MULTIPLE_SELECTION)
                    sb.click(self.NEXT_BUTTON)

        logger.info(f"*****{selected_item}******")


        if self.is_element_present(sb, self.JOB_TITLE_DROP_DOWN):
            sb.click(self.JOB_TITLE_DROP_DOWN)
            sb.click(self.JOB_TITLE_DROP_DOWN_ITEM)
            sb.click(self.NEXT_BUTTON)

        if self.is_element_present(sb, self.ENTER_THE_WORK_EMAILS_OF_COLLEAGUES_HEADER):
            timestamp = int(time.time())
            firstname = f"TestUser{timestamp}"
            lastname = f"LastName{timestamp}"
            email = f"testuser{timestamp}@example.com"

            sb.input(self.coullegue_first_name_input, firstname)
            sb.input(self.coullegue_last_name_input, lastname)
            sb.input(self.coullegue_email_input, email)
            sb.click(self.NEXT_BUTTON)

        if self.is_element_present(sb, self.VIEW_MY_FINGERPRINT_BUTTON):
            sb.click(self.VIEW_MY_FINGERPRINT_BUTTON, timeout=20)

    def go_back_to_prezent(self, sb):
        sb.click(self.BACK_TO_PREZENT_BUTTON, timeout=20)




        



































