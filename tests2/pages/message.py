from base_page import BasePage
from forms.message_form import MessageForm
from forms.companion_form import CompanionForm
from forms.forward_message_companion_form import ForwardMessageCompanionForm
from selenium.webdriver.common.action_chains import ActionChains


from time import sleep

class MessagePage(BasePage):


    def create_dialog(self):

        message_form = MessageForm(self.driver)
        message_form.get_create_dialog_button().click()
    
    def choose_companion(self):
        companion_form = CompanionForm(self.driver)
        companion_form.get_companion_button().click()
        companion_form.get_create_dialog_button().click()

    def choose_companion_forward_message(self):
        forward_message_companion_form = ForwardMessageCompanionForm(self.driver)
        forward_message_companion_form.get_companion_button().click()
        forward_message_companion_form.get_forward_message_button().click()

    def find_message(self, message_text):
        message_form = MessageForm(self.driver)
        ActionChains(self.driver).move_to_element(message_form.get_find_message_input()).perform()        
        message_form.get_find_message_input().send_keys(message_text)
        
