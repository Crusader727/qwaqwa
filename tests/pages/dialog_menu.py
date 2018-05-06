from base_page import BasePage
from forms.dialog_menu_form import DialogMenuForm

class DialogMenuPage(BasePage):


    def delete_dialog(self):

        dialog_menu_form = DialogMenuForm(self.driver)

        dialog_menu_form.delete_dialog().wait_for_visible().get().click()