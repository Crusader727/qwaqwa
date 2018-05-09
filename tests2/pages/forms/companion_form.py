from base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CompanionForm(BaseElement):
    COMPANION_BUTTON = '//div[@data-l="t,participant-add"]'
    CREATE_DIALOG_BUTTON = '//input[@class="button-pro __small mr-2x js-submit"]'
    
    def get_companion_button(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.element_to_be_clickable((By.XPATH, self.COMPANION_BUTTON)))

    def get_create_dialog_button(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.element_to_be_clickable((By.XPATH, self.CREATE_DIALOG_BUTTON)))


