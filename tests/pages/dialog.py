from base_page import BasePage
from forms.dialog_form import DialogForm



class DialogPage(BasePage):
    

    def open_menu(self):
        dialog_form = DialogForm(self.driver)
        dialog_form.get_menu_button().click()
    
    def open_menu_exists(self):
        dialog_form = DialogForm(self.driver)
        return dialog_form.get_menu_button() is not None

    def send_message_button_exists(self):
        dialog_form = DialogForm(self.driver)
        return dialog_form.get_send_message_button() is not None

    def no_messages_text_exists(self):
        dialog_form = DialogForm(self.driver)
        return dialog_form.get_no_messages_text() is not None