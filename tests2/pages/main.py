from base_page import BasePage
from forms.main_form import MainForm

class MainPage(BasePage):
    
    def open_messages(self):
        main_form = MainForm(self.driver)
        main_form.get_message_button().click()