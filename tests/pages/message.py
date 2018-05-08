from base_page import BasePage
from forms.message_form import MessageForm
from forms.companion_form import CompanionForm
from time import sleep

class MessagePage(BasePage):

    def create_dialog(self):

        message_form = MessageForm(self.driver)
        message_form.get_create_dialog_button().click()
    
    def choose_companion(self):
        companion_form = CompanionForm(self.driver)

        companion_form.get_companion_button().click()
        companion_form.get_create_dialog_button().click()
