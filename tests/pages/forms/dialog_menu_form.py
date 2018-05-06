from selenium.webdriver.common.by import By
from base_element import BaseElement

class DialogMenuForm(BaseElement):
    DELETE_DIALOG = (By.XPATH, '//i[@class="tico_img ic ic_remove"]')
