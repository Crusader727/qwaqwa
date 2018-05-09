# -*- coding: utf-8 -*-
from base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DialogForm(BaseElement):
    MENU_BUTTON = '//div[@class="ic inlineBlock ic_info-menu"]'

    SEND_MESSAGE_BUTTON = '//button[@title="Отправить"]'
    MESSAGE_INPUT = "//div[@name='st.txt']"
    
    DELETE_MESSAGE_BUTTON =  "//a[@data-l='t,deleteMsg']"
    EDIT_MESSAGE_BUTTON = "//a[@data-l='t,editMsg']"
    ANSWER_MESSAGE_BUTTON = "//span[@data-l='t,replyToMsg']"
    FORWARD_MESSAGE = "//span[@data-l='t,forward']"

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.element_to_be_clickable((By.XPATH, self.MENU_BUTTON)))
            # EC.visibility_of_element_located((By.XPATH, self.MENU_BUTTON)))
            
   
    def get_send_message_button(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.element_to_be_clickable((By.XPATH, self.SEND_MESSAGE_BUTTON)))

    def get_delete_message_button(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.elements_to_be_clickable((By.XPATH, self.DELETE_MESSAGE_BUTTON)))
       
    def get_edit_message_button(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.elements_to_be_clickable((By.XPATH, self.EDIT_MESSAGE_BUTTON)))
       
    def get_answer_message_button(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.visibility_of_elements_located((By.XPATH, self.ANSWER_MESSAGE_BUTTON)))

    def get_message_input(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.presence_of_element_located((By.XPATH, self.MESSAGE_INPUT)))
        

    def get_forward_message(self):
        return WebDriverWait(self.driver, 30, 1).until(
            EC.element_to_be_clickable((By.XPATH, self.FORWARD_MESSAGE)))

    