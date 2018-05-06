from selenium.webdriver.common.by import By
from base_element import BaseElement

class MainForm(BaseElement):
    MESSAGE_BUTTON = (By.ID, 'msg_toolbar_button')
