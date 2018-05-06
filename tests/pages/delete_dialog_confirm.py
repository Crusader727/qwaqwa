from base_page import BasePage
from forms.message_form import MessageForm
from forms.delete_dialog_confirm_form import DeleteDialogConfirmForm
from forms.companion_form import CompanionForm
from time import sleep

class DeleteDialogConfirmPage(BasePage):


    def delete_dialog(self):

        delete_dialog_confirm_form = DeleteDialogConfirmForm(self.driver)

        delete_dialog_confirm_form.confirm_button().wait_for_visible().wait_for_clickable().get().click()