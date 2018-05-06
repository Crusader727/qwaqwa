from base_page import BasePage
from forms.message_form import MessageForm
from forms.dialog_menu_form import DialogMenuForm
from forms.companion_form import CompanionForm
from time import sleep

class DialogMenuPage(BasePage):


    def delete_dialog(self):

        dialog_menu_form = DialogMenuForm(self.driver)

        dialog_menu_form.delete_dialog().wait_for_visible().wait_for_clickable().get().click()