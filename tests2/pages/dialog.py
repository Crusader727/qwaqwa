from base_page import BasePage
from forms.dialog_form import DialogForm
from selenium.webdriver.common.action_chains import ActionChains



class DialogPage(BasePage):
    

    def open_menu(self):
        dialog_form = DialogForm(self.driver)
        dialog_form.get_menu_button().click()
    
    def write_and_send_message(self, message_text):
        dialog_form = DialogForm(self.driver)
        message_text_field = dialog_form.get_message_input()
        message_text_field.send_keys(message_text)
        dialog_form.get_send_message_button().click()
            
    def delete_message(self):  
        dialog_form = DialogForm(self.driver)
        delete_message_button = self.driver.find_elements_by_xpath(dialog_form.DELETE_MESSAGE_BUTTON)[-1]
        ActionChains(self.driver).move_to_element(delete_message_button).perform()
        delete_message_button.click()   

    def edit_and_send_message(self, message_text):
        dialog_form = DialogForm(self.driver)
        edit_message_button = self.driver.find_elements_by_xpath(dialog_form.EDIT_MESSAGE_BUTTON)[-1]
        ActionChains(self.driver).move_to_element(edit_message_button).perform()
        edit_message_button.click()   
        self.write_and_send_message(message_text)
        
    def answer_message(self, answer_text):
        dialog_form = DialogForm(self.driver)
        answer_message_button = self.driver.find_elements_by_xpath(dialog_form.ANSWER_MESSAGE_BUTTON)[-1]
        ActionChains(self.driver).move_to_element(answer_message_button).perform()
        answer_message_button.click()   
        self.write_and_send_message(answer_text)

    def forward_message(self):
        dialog_form = DialogForm(self.driver)
        forward_message_button = self.driver.find_elements_by_xpath(dialog_form.FORWARD_MESSAGE)[-1]
        ActionChains(self.driver).move_to_element(forward_message_button).perform()
        forward_message_button.click()   
            

    def send_message_button_exists(self):
        dialog_form = DialogForm(self.driver)
        return dialog_form.get_send_message_button is not None