# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from pages.auth import AuthPage
from pages.main import MainPage
from pages.message import MessagePage
from pages.dialog import DialogPage
from pages.dialog_menu import DialogMenuPage
from pages.delete_dialog_confirm import DeleteDialogConfirmPage
from pages.delete_message_confirm import DeleteMessageConfirmPage

from time import sleep

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Tests(unittest.TestCase):
    MESSAGE_TEXT = 'TestNumber1'
    MESSAGE_EDITED_TEXT = ' is_EDITED'
    MESSAGE_ANSWERED_TEXT = ' is_ANSWERED'
    
    
    CREATED_DIALOG_URL = ''

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.sign_in("technopark3","testQA1")
        main_page = MainPage(self.driver)
        main_page.open_messages() # Open chat's window

    def tearDown(self):

        self.driver.quit()

    def create_dialog(self):
        message_page = MessagePage(self.driver)
        message_page.create_dialog() # Create new dialog
        message_page.choose_companion() # Choosing person to start dialog with
        self.CREATED_DIALOG_URL = self.driver.current_url
        return message_page
           
        
    def test_create_and_delete_dialog(self):
        message_page = MessagePage(self.driver)
        message_page.create_dialog() # Create new dialog
        message_page.choose_companion() # Choosing person to start dialog with
        dialog_page = DialogPage(self.driver)
        self.assertEquals(dialog_page.send_message_button_exists(), True)
        self.CREATED_DIALOG_URL = self.driver.current_url
        print self.CREATED_DIALOG_URL
        
        dialog_page.write_and_send_message(self.MESSAGE_TEXT)
        # sleep(5)

        # message_page.find_message(self.MESSAGE_TEXT)
        # # sleep(5)

        # dialog_page.edit_and_send_message(self.MESSAGE_EDITED_TEXT)
        # # sleep(5)
       
        # dialog_page.forward_message()
        # message_page.choose_companion_forward_message()
        # sleep(5)

        # dialog_page.answer_message(self.MESSAGE_ANSWERED_TEXT)
        # sleep(5)

        dialog_page.delete_message()
        delete_message_confirm_page = DeleteMessageConfirmPage(self.driver)
        delete_message_confirm_page.delete_message()
        sleep(5)

        dialog_page.open_menu() # Opening dialog menu in the right top corner
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.delete_dialog()
        delete_dialog_confirm_page = DeleteDialogConfirmPage(self.driver)
        delete_dialog_confirm_page.delete_dialog()
    
    # def test_send_message(self):
    #     MESSAGE_TEXT = 'TestNumber1'  
    #     self.create_dialog()
    #     dialog_page = DialogPage(self.driver)
    #     dialog_page.write_and_send_message(self.MESSAGE_TEXT)
        

    # def test_edit_message(self):
    #     MESSAGE_TEXT = 'TestNumber1'  
    #     MESSAGE_EDITED_TEXT = ' IS_EDITED'      
    #     self.create_dialog()
    #     dialog_page = DialogPage(self.driver)
    #     dialog_page.write_and_send_message(self.MESSAGE_TEXT)
    #     dialog_page.edit_and_send_message(self.MESSAGE_EDITED_TEXT)     
        

    # def test_forward_message(self):
    #     MESSAGE_TEXT = 'TestNumber1'      
    #     message_page = self.create_dialog()
    #     dialog_page = DialogPage(self.driver)
    #     dialog_page.write_and_send_message(self.MESSAGE_TEXT)
    #     dialog_page.forward_message()
    #     message_page.choose_companion_forward_message()
    
    # def test_answer_message(self):
    #     MESSAGE_TEXT = 'TestNumber1'  
    #     MESSAGE_ANSWERED_TEXT = ' IS_ANSWERED'  
    #     self.create_dialog()
    #     dialog_page = DialogPage(self.driver)
    #     dialog_page.write_and_send_message(self.MESSAGE_TEXT)
    #     dialog_page.answer_message(self.MESSAGE_ANSWERED_TEXT)
        

    # def test_delete_message(self):
    #     MESSAGE_TEXT = 'TestNumber1'          
    #     self.create_dialog()
    #     dialog_page = DialogPage(self.driver)
    #     dialog_page.write_and_send_message(self.MESSAGE_TEXT)
    #     dialog_page.delete_message()
    #     delete_message_confirm_page = DeleteMessageConfirmPage(self.driver)
    #     delete_message_confirm_page.delete_message()

       
