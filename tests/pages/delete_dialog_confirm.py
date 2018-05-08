from base_page import BasePage
from forms.delete_dialog_confirm_form import DeleteDialogConfirmForm



class DeleteDialogConfirmPage(BasePage):


    def delete_dialog(self):

        delete_dialog_confirm_form = DeleteDialogConfirmForm(self.driver)

        delete_dialog_confirm_form.get_confirm_button().click()