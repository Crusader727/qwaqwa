# coding=utf-8
from base_page import BasePage
from forms.auth_form import AuthForm

class AuthPage(BasePage):
    url = 'http://ok.ru'

    def sign_in(self, login, password):
        self.driver.get(self.url)

        auth_form = AuthForm(self.driver)
        auth_form.get_login_input().send_keys(login)
        auth_form.get_password_input().send_keys(password)
        auth_form.get_submit_button().click()



