class TemplatesPage:
    TEMPLATE_NAMES = """//*[@id="templates"]//div[@class="templateNameAndShare__content"]/div"""
    ACTIVE_TEMPLATE = """//*[@id="templates"]//button[@class="v-btn v-btn--text theme--light v-size--default select-theme active"]/preceding-sibling::div//div[@class="templateNameAndShare__content"]/div"""

    def get_5template_names(self, sb):
        template_elements = sb.find_elements(self.TEMPLATE_NAMES)
        return [template.text for template in template_elements[:5]]
    def get_active_template(self, sb):
        return sb.get_text(self.ACTIVE_TEMPLATE)
