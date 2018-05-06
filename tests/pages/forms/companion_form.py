from selenium.webdriver.common.by import By
from base_element import BaseElement

class CompanionForm(BaseElement):
    COMPANION_BUTTON = (By.XPATH, '//div[@data-l="t,participant-add"]')
    CREATE_DIALOG_BUTTON = (By.XPATH, '//input[@class="button-pro __small mr-2x js-submit"]')
