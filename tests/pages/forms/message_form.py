
from base_element import BaseElement

class MessageForm(BaseElement):
    CREATE_DIALOG_BUTTON = '//span[@id="chats_create_button"]'
    FIND_DIALOG_INPUT = '//input[@id="ConversationsListSearch_field_query"]'
    SEARCH_RESULT = '//a[contains(@class, "chats_i_ovr")]'

    def get_create_dialog_button(self):
        return self.get_button_by_xpath(self.CREATE_DIALOG_BUTTON)

    def get_find_dialog_input(self):
        return self.get_field_by_xpath(self.FIND_DIALOG_INPUT)
    
    def get_search_result(self):
        return self.existance_of_element_by_xpath(self.SEARCH_RESULT)
        