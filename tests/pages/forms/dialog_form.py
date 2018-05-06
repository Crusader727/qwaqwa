from selenium.webdriver.common.by import By
from base_element import BaseElement

class DialogForm(BaseElement):
    MENU_BUTTON = (By.XPATH, '//div[@class="ic inlineBlock ic_info-menu"]')
