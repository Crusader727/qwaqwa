from base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ForwardMessageCompanionForm(BaseElement):
    COMPANION_BUTTON = '//div[@data-l="t,conv-select"]'
    FORWARD_MESSAGE_BUTTON = '//input[@class="button-pro __small mr-2x js-submit"]'
    
    def get_companion_button(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.element_to_be_clickable((By.XPATH, self.COMPANION_BUTTON)))
   
    def get_forward_message_button(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.element_to_be_clickable((By.XPATH, self.FORWARD_MESSAGE_BUTTON)))


       