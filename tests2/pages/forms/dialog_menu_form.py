
from base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DialogMenuForm(BaseElement):
    DELETE_DIALOG_BUTTON = '//i[@class="tico_img ic ic_remove"]'
   
    def get_delete_dialog_button(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.element_to_be_clickable((By.XPATH, self.DELETE_DIALOG_BUTTON)))
