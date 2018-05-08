
from base_element import BaseElement

class MessageForm(BaseElement):
    CREATE_DIALOG_BUTTON = '//span[@id="chats_create_button"]'

    def get_create_dialog_button(self):
        return self.get_button_by_xpath(self.CREATE_DIALOG_BUTTON)
        