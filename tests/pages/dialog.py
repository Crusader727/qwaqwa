from base_page import BasePage
from forms.dialog_form import DialogForm



class DialogPage(BasePage):

    def open_menu(self):
        dialog_form = DialogForm(self.driver)
        dialog_form.menu_button().wait_for_visible().get().click()
    
    def send_message_button_exists(self):
        dialog_form = DialogForm(self.driver)
        return dialog_form.send_message_button() is not None