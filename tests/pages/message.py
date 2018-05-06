from base_page import BasePage
from forms.message_form import MessageForm
from forms.companion_form import CompanionForm


class MessagePage(BasePage):


    def create_dialog(self):

        message_form = MessageForm(self.driver)

        message_form.create_dialog_button().wait_for_visible().get().click()

    
    def choose_companion(self):
        companion_form = CompanionForm(self.driver)

        companion_form.companion_button().wait_for_visible().get().click()
        companion_form.create_dialog_button().wait_for_visible().get().click()
