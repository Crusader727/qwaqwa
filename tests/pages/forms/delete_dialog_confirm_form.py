
from base_element import BaseElement

class DeleteDialogConfirmForm(BaseElement):
    CONFIRM_BUTTON = '//input[@id="hook_FormButton_menu_op_confirm_btn"]'
    def get_confirm_button(self):
        return self.get_button_by_xpath(self.CONFIRM_BUTTON)
