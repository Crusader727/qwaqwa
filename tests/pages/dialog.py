from base_page import BasePage
from forms.message_form import MessageForm
from forms.dialog_form import DialogForm
from forms.companion_form import CompanionForm
from time import sleep

class DialogPage(BasePage):


    def open_menu(self):

        dialog_form = DialogForm(self.driver)

        dialog_form.menu_button().wait_for_clickable().get().click()