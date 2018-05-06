from selenium.webdriver.common.by import By
from base_element import BaseElement

class AuthForm(BaseElement):
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,sign_in"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="st.password"]')
    LOGIN_INPUT = (By.XPATH, '//input[@name="st.email"]')