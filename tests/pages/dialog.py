from base_page import BasePage
from forms.dialog_form import DialogForm
from forms.attach_form import AttachForm

class DialogPage(BasePage):
    
    def __init__(self, driver):
        super(DialogPage, self).__init__(driver)
        self.dialog_form = DialogForm(self.driver)
        self.attach_form = AttachForm(self.driver)

    def open_menu(self): 
        self.dialog_form.get_menu_button().click()

    def send_message_button_exists(self):
        return self.dialog_form.get_send_message_button_exists()

    def no_messages_text_exists(self):
        return self.dialog_form.get_no_messages_text_exists() 
    
    def send_sticker(self):
        self.dialog_form.get_sticker_button().click()
        self.dialog_form.get_sticker_list_button().click()
        self.dialog_form.get_unsmile_sticker().click()
    
    def message_with_ticker_exists(self):
        return self.dialog_form.get_message_with_sticker()

    def send_music(self):
        self.dialog_form.get_attach_button().click()
        self.attach_form.get_music_button().click()
