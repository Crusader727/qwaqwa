from base_element import BaseElement

class AuthForm(BaseElement):
    SUBMIT_BUTTON = '//input[@data-l="t,sign_in"]'
    PASSWORD_INPUT = '//input[@name="st.password"]'
    LOGIN_INPUT = '//input[@name="st.email"]'

    def get_submit_button(self):
        return self.driver.find_element_by_xpath(self.SUBMIT_BUTTON)
    
    def get_password_input(self):
        return self.driver.find_element_by_xpath(self.PASSWORD_INPUT)
    
    def get_login_input(self):
        return self.driver.find_element_by_xpath(self.LOGIN_INPUT)

