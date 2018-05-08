# -*- coding: utf-8 -*-
from base_element import BaseElement

class DialogForm(BaseElement):
    MENU_BUTTON = '//div[@data-additional-button="js-open-menu"]'
    SEND_MESSAGE_BUTTON = '//button[@title="Отправить"]'
    NO_MESSAGES_TEXT = '//div[@class="stub-empty_t"]'

    def get_menu_button(self):
        return self.get_button_by_xpath(self.MENU_BUTTON)
    def get_send_message_button(self):
        return self.get_button_by_xpath(self.SEND_MESSAGE_BUTTON)
    def get_no_messages_text(self):
        return self.get_field_by_xpath(self.NO_MESSAGES_TEXT)