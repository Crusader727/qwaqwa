from selenium.webdriver.common.by import By
from base_element import BaseElement

class MessageForm(BaseElement):
    CREATE_DIALOG_BUTTON = (By.XPATH, '//span[@id="chats_create_button"]')

