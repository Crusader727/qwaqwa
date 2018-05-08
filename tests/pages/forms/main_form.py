
from base_element import BaseElement

class MainForm(BaseElement):
    MESSAGE_BUTTON = '//div[@id="msg_toolbar_button"]'

    def get_message_button(self):
        return self.get_button_by_xpath(self.MESSAGE_BUTTON)
