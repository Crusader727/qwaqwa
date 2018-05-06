# coding=utf-8


from selenium.webdriver.common.by import By
from base_page import BasePage
from forms.auth_form import AuthForm

class AuthPage(BasePage):
    url = 'http://ok.ru'

    def sign_in(self, login, password):
        self.driver.get(self.url)

        login_form = AuthForm(self.driver)

        login_field = login_form.login_input().wait_for_visible().get()
        login_field.send_keys(login)

        password_field = login_form.password_input().wait_for_visible().get()
        password_field.send_keys(password)

        login_form.submit_button().wait_for_visible().get().click()



