from base_page import BasePage
from forms.main_form import MainForm

class MainPage(BasePage):


    def open_messages(self):

        main_form = MainForm(self.driver)

        main_form.message_button().wait_for_clickable().get().click()
