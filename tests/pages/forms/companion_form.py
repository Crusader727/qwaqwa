from base_element import BaseElement

class CompanionForm(BaseElement):
    COMPANION_BUTTON = '//div[@data-l="t,participant-add"]'
    CREATE_DIALOG_BUTTON = '//input[@class="button-pro __small mr-2x js-submit"]'
    def get_companion_button(self):
        return self.get_button_by_xpath(self.COMPANION_BUTTON)
    def get_create_dialog_button(self):
        return self.get_button_by_xpath(self.CREATE_DIALOG_BUTTON)