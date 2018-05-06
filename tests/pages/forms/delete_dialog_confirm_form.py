from selenium.webdriver.common.by import By
from base_element import BaseElement

class DeleteDialogConfirmForm(BaseElement):
    CONFIRM_BUTTON = (By.XPATH, '//input[@id="hook_FormButton_menu_op_confirm_btn"]')
