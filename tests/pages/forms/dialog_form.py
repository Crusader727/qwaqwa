# -*- coding: utf-8 -*-
from base_element import BaseElement

class DialogForm(BaseElement):
    MENU_BUTTON = '//div[@data-additional-button="js-open-menu"]'
    SEND_MESSAGE_BUTTON = '//button[@title="Отправить"]'
    NO_MESSAGES_TEXT = '//div[@class="stub-empty_t"]'
    MESSAGE_INPUT = '//div[@name="st.txt"]'
    STICKER_BUTTON = '//span[@class="ic ic_smile smiles_w comments_smiles_trigger js-comments_smiles_trigger __new emoji-m"]'
    STICKER_LIST_BUTTON = '//a[@data-l="t,stickersTab"]'
    USMILE_STICKER = '//div[@data-code="#u9b43ee364as#"]'
    ATTACH_BUTTON = 'div.comments_attach_trigger_ic.ic_staple'
    MESSAGE_WITH_STICKER = '//div[@class="msg_sticker js-msg_sticker"]'
    SENT_MESSAGE = '//div[@class="msg_tx"]'


    def get_menu_button(self):
        return self.get_button_by_xpath(self.MENU_BUTTON)

    def get_send_message_button(self):
        return self.get_button_by_xpath(self.SEND_MESSAGE_BUTTON)
    
    def get_send_message_button_exists(self):
        return self.existance_of_element_by_xpath(self.SEND_MESSAGE_BUTTON)

    def get_no_messages_text_exists(self):
        return self.existance_of_element_by_xpath(self.NO_MESSAGES_TEXT)

    def get_message_input(self):
        return self.get_field_by_xpath(self.MESSAGE_INPUT)
    
    def get_sticker_button(self):
        return self.get_button_by_xpath(self.STICKER_BUTTON)

    def get_sticker_list_button(self):
        return self.get_button_by_xpath(self.STICKER_LIST_BUTTON)

    def get_unsmile_sticker(self):
        return self.get_button_by_xpath(self.USMILE_STICKER)
    
    def get_attach_button(self):
        return self.get_button_by_css_selector(self.ATTACH_BUTTON)

    def get_message_with_sticker(self):
        return self.existance_of_element_by_xpath(self.MESSAGE_WITH_STICKER)

    def get_sent_message(self):
        return self.existance_of_element_by_xpath(self.SENT_MESSAGE)
