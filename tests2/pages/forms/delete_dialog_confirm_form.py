
from base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DeleteDialogConfirmForm(BaseElement):
    CONFIRM_BUTTON = '//input[@id="hook_FormButton_menu_op_confirm_btn"]'
    
    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.element_to_be_clickable((By.XPATH, self.CONFIRM_BUTTON)))
