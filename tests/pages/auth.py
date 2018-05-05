# coding=utf-8
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BaseElement(object):
    locator = None
    element = None
    DEFAULT_WAIT_TIME = 30

    def __init__(self, driver):
        self.driver = driver

    def wait_for_presence(self):
        self.element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.presence_of_element_located(self.locator)
        )
        return self

    def wait_for_visible(self):
        self.element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.visibility_of_element_located(self.locator)
        )
        return self

    def wait_for_clickable(self):
        self.element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.element_to_be_clickable(self.locator)
        )
        return self

    def wait_for_alert(self):
        self.element = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            EC.alert_is_present()
        )
        return self

    def is_exists(self):
        try:
            self.driver.find_element(self.locator)
        except Exception as e:
            return False
        return True

    def get(self):
        return self.element

    def __getattr__(self, item):
        def f():
            self.locator = self.__getattribute__(item.upper())
            return self
        return f


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)


class LoginForm(BaseElement):
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,sign_in"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="st.password"]')
    LOGIN_INPUT = (By.XPATH, '//input[@name="st.email"]')


class AuthPage(BasePage):
    url = 'http://ok.ru'

    def sign_in(self, login, password):
        self.driver.get(self.url)

        login_form = LoginForm(self.driver)

        login_field = login_form.login_input().wait_for_clickable().get()
        login_field.click()
        login_field.clear()
        login_field.send_keys(login)

        password_field = login_form.password_input().wait_for_clickable().get()
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_form.submit_button().wait_for_clickable().get().click()




class MainForm(BaseElement):
    MESSAGE_BUTTON = (By.ID, 'msg_toolbar_button')

class MainPage(BasePage):
    # url = 'http://ok.ru'

    def open_messages(self):
        # self.driver.get(self.url)

        main_form = MainForm(self.driver)

        main_form.message_button().wait_for_clickable().get().click()
