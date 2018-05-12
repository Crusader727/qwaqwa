# -*- coding: utf-8 -*-
from base_element import BaseElement

class DialogMenuForm(BaseElement):
    DELETE_DIALOG_BUTTON = '//i[@class="tico_img ic ic_remove"]'
    LEAVE_CHAT_BUTTON = '//i[@class="tico_img ic ic_exit_arrow"]'
    HIDE_CHAT_BUTTON = '//i[@class="tico_img ic ic_hide"]' 

    COMPANION_BUTTON = "//div[@id='hook_Block_ConversationParticipantsAddMenuList']/div[1]/div[2]" 
    ADD_USER_CONFIRM_BUTTON = "//input[@value='Добавить']" 
    DELETE_USER_FROM_GROUP = '//span[contains(@data-l, "participant-remove")]'

    def get_delete_dialog_button(self):
        return self.get_button_by_xpath(self.DELETE_DIALOG_BUTTON)

    #112Nick
    def get_leave_chat_button(self):
        return self.get_button_by_xpath(self.LEAVE_CHAT_BUTTON)

    def get_hide_chat_button(self):
        return self.get_button_by_xpath(self.HIDE_CHAT_BUTTON)
    
    def get_companion_button(self):
        return self.get_button_by_xpath(self.COMPANION_BUTTON)

    def get_add_companion_confirm_button(self):
        return self.get_button_by_xpath(self.ADD_USER_CONFIRM_BUTTON)
    
    def get_delete_companion_button(self):
        return self.get_hidden_input_by_xpath(self.DELETE_USER_FROM_GROUP)
    
